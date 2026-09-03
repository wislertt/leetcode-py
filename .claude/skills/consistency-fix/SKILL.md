---
name: consistency-fix
description: Use when `bake check-consistency` fails with README/file drift, when generated leetcode/ files diverge from JSON templates, when `bake p-gen -f` reports success but drift persists, or when generated files contain stub text (`TODO: Implement` / `O(?)`) despite solved solutions. Covers tag drift, prettier formatting drift, and clobber-window stub poisoning.
---

# Consistency Fix

Resolve drift between committed `leetcode/` files and their JSON template source of truth.

## When to Use

- `bake check-consistency` reports `Drift: leetcode/<problem>/<file>`
- README Tags line stale after tag-list change
- Regenerated file still mismatches after `bake p-gen -f`

## How check-consistency Works

Renames `leetcode/` to `.cache/check-consistency/backup` (rename, not copy) → parallel-generates ALL problems into `.cache/check-consistency/generated` and renames it in as `leetcode/` → runs notebook-to-py conversion **+ lint** → diffs fresh generation against backup → finally restores the original by rename, removes the workdir, and regenerates `docs/problems/` once from the restored tree.

**Interrupted-run recovery:** a run killed mid-window leaves `leetcode/` as freshly generated stubs; the real tree is still at `.cache/check-consistency/backup`. Restore with `rm -rf leetcode && mv .cache/check-consistency/backup leetcode`. The next run refuses to start while that backup exists, so it can never be silently cleaned.

**Docs skip during the check:** the check calls `lint(skip_docs=True)` (also exposed as `bake lint --skip-docs`) because the tree holds stubs then; the finally block regenerates docs once from the restored tree. If stub text still reaches `docs/problems/` with clean git status, some other path generated docs against a stub tree — fix is a plain `uv run python scripts/gen_problems.py`, never a hand-edit (see Class 3).

- `-` lines = backup (committed working tree)
- `+` lines = fresh generated (source of truth)
- **Make committed match generated.**

The lint step is what makes generated diverge from a plain `lcpy gen`. It runs (confirm with `bake check-consistency 2>&1 | grep -E '^❯'`):

- `bunx prettier@latest --write "**/*.{js,jsx,ts,tsx,css,json,json5,yaml,yml,md}"` ← formats README/markdown
- `toml-sort` (.mise.toml, pyproject.toml)
- `ruff format` / `ruff check` (.py only)
- `ty check`, `deptry`, `actionlint`

**Key:** `bake p-gen -f` does NOT run this lint pipeline. It regenerates from the template and runs ruff only. So p-gen output keeps template-raw formatting; check-consistency output is prettier-formatted. That gap IS the drift.

## Diagnose

```bash
bake check-consistency 2>&1 | grep -A25 "Drift:"
```

Read the diff. Three drift classes need different fixes. They can **coexist** on the same file (e.g. tag drift + formatting drift) — fix both.

## Class 1: Tag Drift (README Tags line)

**Symptom:** diff shows only the `**Tags:**` line changed.

**Cause:** README Tags line is built by **reverse-lookup of `tags.json5` arrays**, NOT the `_tags` field in the problem JSON. Adding/removing a problem from a `tags.json5` array makes the committed README stale.

**Fix:** regenerate — tag comes from tags.json5 at gen time.

```bash
bake p-gen -p {problem_name} -f
```

Tag drift is the ONLY class that regen alone fixes. After regen, re-check — formatting drift may still remain (see Class 2).

## Class 2: Formatting Drift (prettier)

**Symptom:** diff shows blank lines added/removed, list-indent changes (e.g. nested bullet `  -` → `    -`), blank lines inserted around `**Explanation:**`, or trailing whitespace/blank-line changes.

**Cause:** README template emits raw markdown (double-blanks, 2-space nested indent, no blanks around emphasis). check-consistency runs `prettier --write` over `.md`, which normalizes: collapses double-blanks, reindents nested lists to 4 spaces, pads block-level emphasis, trims trailing blanks. p-gen skips prettier → committed keeps raw form → mismatch.

**GOTCHA — regen alone CANNOT fix this.** `bake p-gen -f` will report `N files left unchanged` / `All checks passed` — false success. Regen reproduces the same raw formatting.

**Fix (preferred):** run the same prettier over the drifted file directly. Matches generated exactly, no manual guessing.

```bash
bunx prettier@latest --write "leetcode/{problem}/README.md"
```

**GOTCHA — prettier is a NO-OP inside code fences.** Prettier never normalizes fenced content, so if the drift lives inside a ``` block (e.g. the generated example pads/aligns inline comments: `mapSum.sum("ap");           // ...` vs committed unpadded — batch 19b: map_sum_pairs, recurred after a batch-19 prettier "fix"), prettier --write reports "unchanged" and cannot fix it no matter how many times it runs. Signal: drift lines look byte-identical in the Drift box (the difference is fence-internal whitespace/alignment). Fall through to the regen route:

```bash
cp leetcode/{problem}/solution.py /tmp/solution_backup.py
bake p-gen -p {problem_name} -f            # emits the fence content as generated
cp /tmp/solution_backup.py leetcode/{problem}/solution.py
bunx prettier@latest --write "leetcode/{problem}/README.md"   # normalize the non-fence markdown
rm -f leetcode/{problem}/playground.ipynb  # legacy trees: see Post-Regen Cleanup
```

Committed must equal generated-after-lint; when the drift source is fence content, only regen produces it.

**Multi-problem variant:** when the JSON example content itself changed by hand (e.g. fence-balancing after a scraper bug), regenerating READMEs for several problems at once, do NOT restore only `solution.py` after `p-gen -f` — hand-tuned `test_solution.py` / `helpers.py` would be clobbered too. Back up the whole problem dir, regen, restore everything except `README.md`:

```bash
rm -rf /tmp/lcpy_bak_{problem}
cp -r leetcode/{problem} /tmp/lcpy_bak_{problem}
bake p-gen -p {problem} -f
for f in /tmp/lcpy_bak_{problem}/*; do
  base=$(basename "$f")
  [ "$base" != "README.md" ] && cp "$f" "leetcode/{problem}/$base"
done
for f in leetcode/{problem}/*; do
  base=$(basename "$f")
  if [ ! -e "/tmp/lcpy_bak_{problem}/$base" ] && [ "$base" != "README.md" ]; then rm "$f"; fi
done
bunx prettier@latest --write "leetcode/{problem}/README.md"
```

**Fix (fallback, no bun):** apply the diff hunks by hand — collapse double-blanks to single, reindent nested list items to 4 spaces, pad blank lines around block emphasis, strip trailing blanks (keep one newline at EOF).

```bash
# strip trailing blank lines, keep single trailing newline
printf '%s\n' "$(cat leetcode/{problem}/README.md)" > leetcode/{problem}/README.md
```

For non-markdown files, match the linter that owns the format: `toml-sort` for `.toml`, `ruff format` for `.py`.

## Class 3: Stub Content (clobber-window poisoning)

**Symptom:** generated files contain `# TODO: Implement <method>` and `# Time: O(?)` while git status is clean and `solution.py` on disk holds the real implementation. Check instantly with:

```bash
grep -rl "TODO: Implement" docs/problems/ | wc -l      # docs poisoned
grep -rl "TODO: Implement" leetcode/*/solution.py | wc -l  # leetcode/ still clobbered
```

**Cause:** a generator ran while `leetcode/` held template stubs. The classic case (2026-09-03, 1403/1404 pages poisoned): `check-consistency` regenerated `leetcode/` as stubs and `lint()` ran `gen_problems.py` against that stub tree before the restore. The check now guards this (lint skips docs gen mid-check, finally regenerates from the restored tree), but the window still exists for ANY other path that regenerates docs while `leetcode/` is stubbed — e.g. a `p-gen -f` followed by a docs regen before the solution is restored.

**Fix:** regenerate the poisoned artifacts from the restored (real) tree — never hand-edit stub text out:

```bash
uv run python scripts/gen_problems.py
```

**Prevention (already in place, do not remove):** `bakefile.py` `check_consistency` calls `lint(skip_docs=True)` mid-check and re-runs `gen_problems.py` after the restore in the `finally` block. If you touch that code path, keep both halves.

**Interpretation rule:** stub text in ANY generated artifact with a clean git status = the artifact was written during a clobber window. Git history cannot tell you this — the file looks legitimately generated. Only the grep catches it.

## Post-Regen Cleanup (after ANY mid-batch `p-gen -f`)

If you regenerate a problem after pre-commit has already run (e.g. fixing drift found at finalization), the fresh generation adds two artifacts the committed tree may not have:

1. **README prettier drift re-appears** — p-gen emits template-raw markdown. Re-run `bunx prettier@latest --write "leetcode/{problem}/README.md"` right after the regen, before the next check-consistency (batch 4, 7, 19: recurring).
2. **A stray `playground.ipynb`** appears for legacy problems whose committed tree only has `playground.py` (batch 19: map_sum_pairs). Delete it unless you intend to migrate the tree to notebook layout:

```bash
bunx prettier@latest --write "leetcode/{problem}/README.md"
rm -f leetcode/{problem}/playground.ipynb   # legacy trees: p-gen -f regenerates the notebook
```

## Common Mistakes

| Mistake                                                    | Reality                                                                                                                          |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Edit JSON `_tags` to fix tag drift                         | Tags line comes from `tags.json5` arrays, not `_tags`. Won't help.                                                               |
| Run `bake p-gen -f` to fix formatting drift                | p-gen skips prettier → reproduces same raw formatting → no change. Run `prettier --write` on the drifted file.                   |
| Strip blanks manually when prettier available              | Prettier also reindents lists and pads emphasis — manual blank-strip misses hunks. Use `bunx prettier --write`.                  |
| Assume only blank lines drift                              | Prettier reformats indent + spacing too. Read every hunk, don't stop at the first blank-line hunk.                               |
| Edit generated file for content drift                      | Content drift = JSON/template wrong. Fix the JSON, regenerate. Only formatting drift is fixed in the generated file directly.    |
| Run prettier on fence-internal drift and expect a fix      | Prettier never normalizes inside code fences — reports "unchanged". Fence drift (comment alignment) needs the regen route above. |
| Assume "All checks passed" from p-gen means drift resolved | p-gen success ≠ check-consistency success. Only `bake check-consistency` passing is real.                                        |
| Fix one drift class, stop                                  | Tag + formatting drift coexist. After any fix, re-run check-consistency until PASSED.                                            |
| Trust clean git status = clean generated files             | Stub poisoning looks like a normal generated file. Grep for `TODO: Implement` in docs/problems/ when anything smells off.        |
| Hand-strip `# TODO: Implement` out of docs pages           | The page is stale, not wrong. Regen from the real tree (`uv run python scripts/gen_problems.py`); hand edits get overwritten.    |

## Verify

```bash
bake check-consistency
# → ✅ Consistency check PASSED: all files match JSON source of truth
```
