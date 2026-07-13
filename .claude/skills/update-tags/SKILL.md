---
name: update-tags
description: Use ONLY when user explicitly requests "update tags" or "/update-tags", or after running .claude/.dev/update_tags.py and seeing "Missing" or "Removed" discrepancy lines. Reconciles the tag sync between source lists and tags.json5.
---

# Update Tags

## Overview

Two layers, one direction of truth:

- **Source (input)** — `.claude/.dev/problem_lists/*.py`. Each defines `tag_name` + `problems_list` of `(problem_number, "Title")` tuples. These are the canonical membership lists. `__init__.py` exposes them via `available_lists`.
- **Output (sink)** — `src/leetcode_py/cli/resources/leetcode/json/tags.json5`. JSON5 with comments. Lists problem-name strings per tag, plus sub-tag references like `{ tag: "neetcode-150" }`. Consumed by the CLI at runtime.

`update_tags.py` diffs the two and prints discrepancies. It **never edits files** — a human resolves each line at the correct layer.

## The Core Decision (read before touching anything)

The script prints two kinds of lines. They have **different fix locations**:

| Script line                                 | Meaning                      | Where to fix                                          |
| ------------------------------------------- | ---------------------------- | ----------------------------------------------------- |
| `Missing N: [...]`                          | in source, not in tags.json5 | **tags.json5** (add entries)                          |
| `Removed N: [...] (not included in update)` | in tags.json5, not in source | **either layer** — decide via `_tags.list` (see trap) |

**Iron rule:** `Missing` → edit `tags.json5`. `Removed` → **check the problem's `_tags.list` first** — fix source if membership confirmed, else delete from tags.json5. Never guess the direction.

## The "Removed" Trap (where data gets lost)

A "Removed" line means tags.json5 lists a problem the source list doesn't. **Do not reflexively add a tuple to source** — a "Removed" line is two opposite cases, and you must decide which before touching anything:

| Case                                                  | Signal                                              | Fix                                              |
| ----------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------ |
| Source list lagging (problem genuinely belongs here)  | flagged tag **IS** in the problem JSON `_tags.list` | **source** — add `(number, "Title")` tuple       |
| tags.json5 entry bogus (problem does not belong here) | flagged tag **NOT** in `_tags.list`                 | **tags.json5** — delete the entry (confirm user) |

**Decide via the problem's own metadata.** Read `src/leetcode_py/cli/resources/leetcode/json/problems/<name>.json` → the `_tags.list` array is the problem's self-declared roadmap membership. It is a **stronger** signal than the tags.json5 entry you're auditing — a problem knows which roadmaps claim it.

- flagged tag ∈ `_tags.list` → the problem considers itself a member; the source list just hasn't caught up. Add the tuple to source.
- flagged tag ∉ `_tags.list` → the tags.json5 entry was likely added by mistake. Do **not** propagate it to source. Confirm with the user, then delete the entry from that tag's array in tags.json5.

The script deliberately refuses to auto-delete ("not included in update") so a human makes this call. Both wrong directions are permanent: deleting a real entry hides it (source lacks it, so `Missing` never fires to restore); adding a bogus tuple to source cements a mistake the script can no longer flag. The `_tags.list` check is what tells you which direction is safe.

**To get the number + exact title:** same JSON → `problem_number` + `problem_title` (proper-cased, e.g. `"Last Stone Weight II"`). Note `problem_name` is the snake_case **slug** — do NOT use it as the title. Match the casing already used in that source file.

## Inheritance Asymmetry (expect false positives)

tags.json5 **inherits** — `{ tag: "neetcode-150" }` inside `neetcode-250` recursively pulls in all of neetcode-150. Source lists do **not** inherit (`neetcode_250.py` does not auto-include `neetcode_150.py`).

Consequence: a "Removed" line on an inheriting tag (e.g. neetcode-250) is frequently a **false positive** — the problem enters `existing` only via the inherited sub-tag reference, and the source-side set has no matching inheritance. Example tell: a problem flagged "Removed" for neetcode-150 but **not** for neetcode-250 means its tuple is in `neetcode_250.py` but missing from `neetcode_150.py`.

Fix is still source-side: add the tuple to the source list(s) that should contain it. If the same problem is "Removed" across multiple tags, add the tuple to each relevant source file.

## Workflow

1. **Run:** `uv run python .claude/.dev/update_tags.py`
2. **If `No changes found`** → done. Delete `.claude/.dev/update_tags.json` if it exists. Stop.
3. **For each `Missing` line:** add the listed problem-name strings to that tag's array in `tags.json5`, in **alphabetical order**. Use `Edit`, not a full rewrite — preserve the `// comment` above each tag block and the JSON5 formatting (quoted keys for hyphenated names like `"neetcode-250"`, bare keys for `grind`; strings as `"snake_case"`).
    - **Find the right block first.** Many tag arrays share identical entries (`maximum_subarray` appears in 4+ blocks; `majority_element`, `minimum_path_sum`, etc. repeat across roadmaps). A `grep -n` hit + the nearest `"tag": [` header above it do **not** prove the line lives in that block — arrays can stretch 60+ lines and the header above may belong to a different tag. Before `Edit`, `Read` the target block's full `[ ... ]` span and copy 2–3 consecutive anchor lines **from inside that block** as `old_string`. Verify the anchor is unique to the target block by eyeballing the span, not by assumption.
4. **For each `Removed` line:** run the `_tags.list` decision from the trap above — **before** any edit. Add the tuple to source only if membership is confirmed (`_tags.list` contains the flagged tag). Otherwise delete the entry from that tag's array in tags.json5, after confirming with the user. Keep the source file's existing ordering convention (neetcode_150.py is sorted by number; neetcode_250.py and grind.py are topical — append if unsure).
5. **Re-run** the script. Expect `No changes found`. Loop until clean. This is not cosmetic — a re-run that **surfaces a new** `Removed`/`Missing` on a tag you did _not_ intend to touch is the tell-tale sign of a wrong-block edit (step 3 trap). If that happens, your last edit landed in the wrong array: revert it and re-apply in the correct block.
6. **Cleanup:** `rm .claude/.dev/update_tags.json`

## Common Mistakes

- **Deleting "Removed" entries from tags.json5 without checking `_tags.list`** — a real tracked problem vanishes permanently. But the opposite is equally bad…
- **Adding a source tuple without checking `_tags.list`** — a "Removed" line is not a command to add. If the problem's own `_tags` metadata does not claim membership in the flagged roadmap, the tags.json5 entry is the bug, not the source list. Propagating a bogus entry to source cements the mistake (script can no longer flag it). Read `_tags.list` first; it tells you which direction is safe.
- **Full-rewrite of tags.json5 via `json.dump`** — destroys the `//` comments and JSON5 formatting. Always surgical `Edit`.
- **Unsorted insertion into tags.json5** — each tag's array is alphabetical; keep it so.
- **Wrong title casing in source tuple** — copy `problem_title` (proper-cased) from the JSON, not `problem_name` (snake_case slug). Match the file's existing entry style (e.g. `"Smallest Range Covering Elements from K Lists"`).
- **Trusting one script run after edits** — always re-run until `No changes found`; a single fix can surface/resolve related lines.
- **Editing the wrong tags.json5 block** — entries like `maximum_subarray`, `majority_element`, `minimum_path_sum` recur across many tag arrays. Picking an `Edit` anchor from `grep` output without reading the target block's `[ ... ]` span easily lands the edit in a neighboring array (e.g. inserting into `algo-master-75` when you meant `neetcode-250`). The re-run then shows a _new_ discrepancy on the unintended tag. Read the block, anchor inside it, verify uniqueness by inspection.

## Files

- Script: `.claude/.dev/update_tags.py`
- Source lists: `.claude/.dev/problem_lists/*.py` (+ `__init__.py` → `available_lists`)
- Output: `src/leetcode_py/cli/resources/leetcode/json/tags.json5`
- Problem metadata (number/title lookup): `src/leetcode_py/cli/resources/leetcode/json/problems/<name>.json`
- Temp file (delete after): `.claude/.dev/update_tags.json`
