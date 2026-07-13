---
name: consistency-fix
description: Use when `bake check-consistency` fails with README/file drift, when generated leetcode/ files diverge from JSON templates, or when `bake p-gen -f` reports success but drift persists. Covers tag drift and prettier formatting drift.
---

# Consistency Fix

Resolve drift between committed `leetcode/` files and their JSON template source of truth.

## When to Use

- `bake check-consistency` reports `Drift: leetcode/<problem>/<file>`
- README Tags line stale after tag-list change
- Regenerated file still mismatches after `bake p-gen -f`

## How check-consistency Works

Backs up `leetcode/` → deletes it → regenerates ALL via `lcpy gen --all` → runs notebook-to-py conversion **+ lint** → diffs fresh generation against backup.

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

Read the diff. Two drift classes need different fixes. They can **coexist** on the same file (e.g. tag drift + formatting drift) — fix both.

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

**Fix (fallback, no bun):** apply the diff hunks by hand — collapse double-blanks to single, reindent nested list items to 4 spaces, pad blank lines around block emphasis, strip trailing blanks (keep one newline at EOF).

```bash
# strip trailing blank lines, keep single trailing newline
printf '%s\n' "$(cat leetcode/{problem}/README.md)" > leetcode/{problem}/README.md
```

For non-markdown files, match the linter that owns the format: `toml-sort` for `.toml`, `ruff format` for `.py`.

## Common Mistakes

| Mistake                                                    | Reality                                                                                                                       |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Edit JSON `_tags` to fix tag drift                         | Tags line comes from `tags.json5` arrays, not `_tags`. Won't help.                                                            |
| Run `bake p-gen -f` to fix formatting drift                | p-gen skips prettier → reproduces same raw formatting → no change. Run `prettier --write` on the drifted file.                |
| Strip blanks manually when prettier available              | Prettier also reindents lists and pads emphasis — manual blank-strip misses hunks. Use `bunx prettier --write`.               |
| Assume only blank lines drift                              | Prettier reformats indent + spacing too. Read every hunk, don't stop at the first blank-line hunk.                            |
| Edit generated file for content drift                      | Content drift = JSON/template wrong. Fix the JSON, regenerate. Only formatting drift is fixed in the generated file directly. |
| Assume "All checks passed" from p-gen means drift resolved | p-gen success ≠ check-consistency success. Only `bake check-consistency` passing is real.                                     |
| Fix one drift class, stop                                  | Tag + formatting drift coexist. After any fix, re-run check-consistency until PASSED.                                         |

## Verify

```bash
bake check-consistency
# → ✅ Consistency check PASSED: all files match JSON source of truth
```
