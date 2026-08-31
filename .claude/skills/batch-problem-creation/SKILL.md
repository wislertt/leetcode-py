---
name: batch-problem-creation
argument-hint: "[count]"
description: Batch creation workflow for multiple LeetCode problems - loops through problem creation, solution implementation, and quality assurance for a specified count. Accepts optional count argument (e.g., /batch-problem-creation 10) or the keyword "unscrapable" to drain the not-yet-done queue in unscrapable.py via web-sourced data (/batch-problem-creation unscrapable). Defaults to 5 if no argument. Use ONLY when user explicitly requests batch creation via /batch-problem-creation command.
---

# Batch Problem Creation Command

## Assistant Workflow

1. **Parse arguments**: If `$ARGUMENTS` contains the keyword `unscrapable`, run the **Creating Unscrapable Problems from the Web** flow (bottom of this file) instead of the normal loop. Otherwise use `$ARGUMENTS` as count (valid integer); default 5 if absent
2. **Loop**: for each problem — find next problem, follow @.claude/skills/problem-creation.md, implement the optimal solution, run quality assurance per @.claude/skills/test-quality-assurance.md
3. **Finalize the whole batch**: pre-commit, tag sync check, consistency check (in order — see Batch Finalization)
4. **Summarize**: batch results + skill improvement suggestions

**CRITICAL**: Read test-quality-assurance.md before executing quality assurance for ANY problem — do not rely on memory of the workflow.

## Step 1: Problem Creation Loop

### 1.1: Find Next Problem

**GOTCHA — never hand-copy the number into the scrape.** Transcribing `#214` as `257` scrapes the wrong problem silently and wastes a full cycle. Chain the scrape off the script output — and capture the `Tag:` line in the same pass (it feeds `_tags.list` in the JSON; piping to grep twice drops it):

```bash
OUT=$(uv run python .claude/.dev/next_problem.py)
N=$(echo "$OUT" | grep -oE '#[0-9]+' | tr -d '#')
TAG=$(echo "$OUT" | grep -oE 'Tag: [a-z0-9-]+' | cut -d' ' -f2)
uv run lcpy scrape -n "$N"   # report: #N, tag: $TAG
```

The script automatically excludes known unscrapable problems.

### 1.2: Create Problem Files

Follow @.claude/skills/problem-creation.md end to end: scrape → transform (with images) → JSON in `src/leetcode_py/cli/resources/leetcode/json/problems/{problem_name}.json` → tags.json5 insert → `bake p-gen -p {problem_name}` → fix JSON (never generated files) and re-run until clean.

All gotchas live there, including the batch-only steps in its **Batch Flow Notes** section: premium/SQL scrape-failure queueing, rtk tee truncation, repo-wide lint batching cadence, and the ruff-clean-from-start rules. The `ast.literal_eval` and E501 test-case rules are in its JSON Template Format section. Do not re-derive them here.

### 1.3: Implement Optimal Solution

Implement ONE optimal solution in the single `Solution` class in `solution.py` (design problems: the custom class only) — before QA, so tests must pass there. Write it ruff/ty-clean up front per problem-creation.md Batch Flow Notes; `bake lint` during QA may not surface pre-commit-level findings, and fixing at finalization costs a late fix cycle.

### 1.4: Quality Assurance

Follow the 6-step process in @.claude/skills/test-quality-assurance.md (backup → regen → restore solution → lint → test → cleanup). Per-problem chain, lint deferred per the batching cadence in problem-creation.md Batch Flow Notes:

```bash
cp -r leetcode/{problem_name} leetcode/{problem_name}_backup && \
bake p-gen -p {problem_name} -f && \
cp leetcode/{problem_name}_backup/solution.py leetcode/{problem_name}/solution.py && \
bake p-test -p {problem_name} 2>&1 | tail -1 && \
rm -rf leetcode/{problem_name}_backup
```

The solution is already implemented (1.3), so tests MUST pass here — a failure means bad JSON test expectations or a wrong solution (see problem-creation.md gotchas), not an "incomplete solution".

## Step 2: Batch Finalization (MANDATORY — after ALL problems)

Three gates in order. Do NOT skip any.

### 2.1: Pre-Commit (converts notebooks to .py)

```bash
pre-commit run -a
```

- `nb-to-py` converts every `leetcode/**/playground.ipynb` to `playground.py` and deletes the `.ipynb`; `lint` runs the full pipeline (sort_tags, check_tag_problems, gen_catalog, lint)
- Fix failures and re-run until clean
- **Why first**: `bake check-consistency` diffs `playground.py`, not `playground.ipynb` — notebooks MUST be converted before the consistency check

### 2.2: Tag Sync Check

```bash
uv run python .claude/.dev/update_tags.py
```

- Expect `No changes found in any of the specified tags.` — that IS the pass state (tags were synced per-problem during creation). `Missing`/`Removed` lines only appear on a dirty run
- A clean run creates NO `.claude/.dev/update_tags.json` — the `rm` no-ops. Remove the temp file if it exists after a dirty run
- **Gate semantics**: the gate counts only **Missing** lines. Pre-existing `Removed` lines do NOT block it — surface them to the user instead of silently resolving them
- **Warning**: do not resolve `Removed` lines on curated lists (neetcode-150, neetcode-250, blind-75, etc.) without the user's call — the `_tags.list` membership check is circular for batch-created problems and following it once cemented bogus tuples into curated lists. Ground truth = source-list membership by problem number
- If any `Missing`/`Removed` lines appear: **read and follow @.claude/skills/update-tags.md**

### 2.3: Consistency Check

```bash
bake check-consistency
```

- Regenerates ALL problems from JSON into a temp dir, converts notebooks, lints, then diffs against the working tree (original `leetcode/` is restored afterwards — solutions preserved)
- Expect `✅ Consistency check PASSED: all files match JSON source of truth`
- On drift (`Drift: leetcode/<problem>/<file>`): **read and follow @.claude/skills/consistency-fix.md**
- Loop until PASSED. `bake p-gen -f` reporting success does NOT mean consistency passes — only this command passing is real
- **GOTCHA — a FAILED run can leave `leetcode/` as regenerated stubs.** `Restoring original leetcode/...` runs at the END of the pipeline; if the run aborts at its lint stage (ruff/ty error mid-batch), the restore never executes and the working tree keeps freshly generated TODO-stub solutions for EVERY problem. After any consistency failure, verify before continuing: `grep -l "TODO: Implement" leetcode/*/solution.py` — any hit means solutions were wiped (rewritable from session context or a /tmp copy; take the copy BEFORE the first consistency run, not after a failure). Only the PASSED run restores reliably
- **GOTCHA — flat `cp` can silently truncate the safety snapshot.** `cp leetcode/*/solution.py /tmp/dir/` copied exactly 1 file in one run (glob expansion mangled, likely by the rtk hook) — a silently-empty snapshot defeats its purpose. Use a per-problem loop and verify the count:

```bash
mkdir -p /tmp/batch_solutions_$(date +%Y%m%d)
for d in leetcode/*/; do
  [ -f "$d/solution.py" ] && cp "$d/solution.py" "/tmp/batch_solutions_$(date +%Y%m%d)/$(basename "$d")_solution.py"
done
ls /tmp/batch_solutions_$(date +%Y%m%d) | wc -l   # must equal number of problems
```

- **Warning**: `bake p-gen -p {problem_name} -f` overwrites `solution.py` with the TODO stub — backup and restore around ANY regen:

```bash
cp leetcode/{problem_name}/solution.py /tmp/solution_backup.py
bake p-gen -p {problem_name} -f
cp /tmp/solution_backup.py leetcode/{problem_name}/solution.py
```

## Step 3: Batch Summary

Report: total created, success rate, failed problems with reasons, finalization results. Then re-test all batch problems with `bake p-test -p {name}` and report counts.

### 3.1: Skill Improvement Suggestions

After the summary, review the run and **suggest** candidate updates to any skill used this session (batch-problem-creation, problem-creation, test-quality-assurance, update-tags, consistency-fix). Scope is the best overall skill, not just additions: new failure modes AND cuts — sections that wasted effort, duplicated another skill, or went stale. When in doubt, prefer deleting or merging over appending.

- **FIRST: read the suggestion log memory** (`skill-suggestions-log` in auto-memory). A suggestion already recorded there is BLOCKED from re-proposal — if it was applied, re-suggesting means the skill text failed (say which wording); if it was skipped, the user chose not to act (do not resurrect). Aim for ZERO suggestions on a batch that hit no genuinely new failure mode — the list should shrink batch over batch, not stay constant
- **Suggestion only. NEVER edit skill files** — the user decides and updates skills themselves (unless the user explicitly instructs the edit this session; then record the applied change in the log)
- **Bar for additions**: only what (a) will recur in future runs AND (b) existing skill content misses. Reject re-derivations (an existing gotcha catching the issue = skill working), refinements/widenings of working gotchas, niche one-offs (a greppable reference JSON suffices), run trivia. Test: name the exact step that failed AND the cycle it cost — no cost, no suggestion
- **Bar for cuts**: anything the run showed to be redundant, misleading, or unused — including steps followed out of habit that added no value
- If nothing new was learned, say so explicitly — do not invent suggestions

## Error Handling

- **Continue the batch** when a problem fails — log the reason, move to the next, note it in the summary
- **NEVER edit generated files** (helpers.py, test_solution.py, README.md, ...) — fix the JSON template and regenerate. The ONLY exception is `solution.py`
- **Scrape failures**: premium → unscrapable queue; SQL → `NON_PYTHON_PROBLEMS`; transient API → retry once

## Success Criteria

Each problem: all files generated, optimal solution implemented (single class), 12+ test cases, lint clean, `bake p-test` passes, QA chain run with solution preserved.

The batch: `pre-commit run -a` passes, tag sync clean, `bake check-consistency` PASSED, all problems still pass `bake p-test` after finalization.

## Unscrapable Problems Management

### Queue placement

`unscrapable.py` has a divider: `# ======= Add new unscrapable problems below this line.` — entries BELOW it are the todo queue (discovery order), entries above are already handled. **Append new discoveries at the BOTTOM of the below-divider queue** (appending at the top re-orders the queue against discovery order). Format: `(problem_number, "kebab-name")`. `next_problem.py` skips them automatically. Non-Python problems (SQL, shell) go to `NON_PYTHON_PROBLEMS` in the same file — never the queue.

### Premium clusters

Consecutive premium problems are common (e.g. 243-256). When two neighbors in a row fail, probe the whole range in a loop BEFORE adding exclusions one-by-one, then batch-add the failures:

```bash
for n in 247 248 249 250 251 252 253 254 255; do
  r=$(uv run lcpy scrape -n $n 2>&1 | head -c 30)
  case "$r" in Error*) echo "$n FAIL";; *) echo "$n OK";; esac
done
```

Sanity-check with a known-scrapable number first (e.g. `uv run lcpy scrape -n 205`) — every number failing means a broken network session, not a premium cluster.

### Creating Unscrapable Problems from the Web

When triggered via the `unscrapable` keyword, or any explicit request to work through `unscrapable.py` entries (user-driven batch, no `next_problem.py`):

0. **Fetch ALL problem statements upfront, via `curl` — no Playwright needed.** `raw.githubusercontent.com` serves plain static text; `curl -s '<doocs-url>'` returns the full markdown faster than a browser and keeps the shared Playwright MCP free for other agents (Playwright cannot run parallel sessions). Do NOT use the `web_reader` MCP tool — user rule. Playwright is FALLBACK ONLY, for sources needing a real browser (or if curl is blocked) — when needed, request it as the flow's first tool call so the permission prompt lands before any file work. With either method: fetch every statement back to back at the start, then build the batch offline — no web dependency mid-loop
1. **Find not-yet-done entries**: entries below the divider are the todo queue; entries above are handled. Still verify against `leetcode/` dirs, `src/.../json/problems/`, and `tags.json5` — the divider may be stale
2. **Determine tags from source lists**: grep the problem number in `.claude/.dev/problem_lists/*.py` (Python lists, not `.list` files). The matching list gives the tag — usually `neetcode` for the NeetCode All queue. Never stamp roadmap tags the number does not belong to
3. **Fetch problem data** (see step 0 — fetch upfront via curl):
    - Primary: doocs/leetcode raw markdown mirror — carries the CURRENT official wording, examples, constraints, and topics (front matter `tags:`). URL pattern: `https://raw.githubusercontent.com/doocs/leetcode/main/solution/0100-0199/0156.Binary%20Tree%20Upside%20Down/README_EN.md` (century folder `0100-0199`, zero-padded number, URL-encoded title). `curl -s '<url>' | head -c 4000` — description + first solution. Title-guess 404? List the exact folder via GitHub API: `curl -s https://api.github.com/repos/doocs/leetcode/contents/solution/0200-0299 | grep '"name"'`
    - Fallback: `https://leetcode.ca/all/{N}.html` (older wording, usually no constraints) — curl first; Playwright only if it needs JS
    - **Playwright GOTCHA** (fallback only): `browser_evaluate` hangs on raw.githubusercontent pages (plain-text doc; eval stalls past 120s). Do NOT evaluate: navigate, then read the auto-saved snapshot at `.playwright-mcp/page-*.yml` — `head -c` the file
    - **Watch for revised statements**: doocs mirrors the current official text, which may differ from the classic version (163 Missing Ranges now returns `list[list[int]]` ranges and is Easy). Model the JSON on the fetched text, never on memory
    - **Cross-check the queue slug against the doocs folder name**: queue names are hand-entered and can be flat wrong (302 was queued as `smallest-range-covering-elements-from-k-arrays`; real 302 is Smallest Rectangle Enclosing Black Pixels — the K-Lists problem is 632, already in the repo). When the GitHub API listing or the fetched title disagrees with the queue tuple, the QUEUE is wrong: model the JSON on the real problem and correct the kebab-name when closing the loop in step 7
4. **Machine-verify every expectation** before writing the JSON (see problem-creation.md gotcha). Premium problems ship only 2-3 official examples, so most test cases are hand-invented — run a reference implementation over all of them (`uv run python` with `TreeNode[int].from_list` for tree round-trips)
    - **Design problems** (`solution_class_name` != `Solution`, e.g. 244 WordDistance): model on `design_hit_counter.json` — ops-sequence test cases (`['WordDistance', 'shortest', ...]` + per-op inputs), run helper instantiates the class mid-sequence
    - **Exponential-output problems** (result list grows 2^n, e.g. 247): use the `n_queens.json` dual-method pattern — method 1 asserts full SORTED lists for small n, method 2 asserts result COUNT only for large n (extra `assert_<name>_count` in `helpers_content`)
5. **Insert into tags.json5 carefully**: the `neetcode:` block begins with a metadata object (`{ tag: "neetcode-250", },`) before the string entries. Filter to quoted-string lines when bisecting; verify with `git diff` + `bake lint` (sort_tags), not a hand-rolled sort assert
6. Continue with the normal loop (p-gen, solution, QA, finalization)
7. **Close the loop in `unscrapable.py`**: once created and finalized, move the tuple ABOVE the divider. Only move what actually got created — non-Python problems go to `NON_PYTHON_PROBLEMS`, never the handled section. Entries found already-created during the step-1 staleness check also move up at close time (verify they actually exist in `leetcode/`, the JSON dir, and tags before moving). If step 3 found the queue entry misnamed, fix the kebab-name in the moved tuple
