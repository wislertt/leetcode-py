---
name: pr-ci-triage
description: Use when reviewing a contributor PR in this repo, drafting a reply to a PR, or when PR CI checks fail (pre-commit, test-reproducibility). Maps each CI failure to the exact bake/pre-commit fix command so replies skip log archaeology. Use ONLY for PR/issue triage on this repository.
---

# PR CI Triage

Diagnose contributor PR CI failures and draft the maintainer reply.

## Flow

1. `gh pr view <N> -R wislertt/leetcode-py --json author,title,body,headRefName,maintainerCanModify,files`
2. `gh pr checks <N> -R wislertt/leetcode-py` — list failed jobs.
3. For each failed job: `gh run view --job <job_id> -R wislertt/leetcode-py --log-failed`, then grep `##\[error` and the lines just before it.
4. Map to the failure table below. One root cause usually fails multiple jobs.
5. Draft reply per the Reply Template. Do not post until the user approves.

## Failure → Fix Table

| Symptom in log                                         | Root cause                                             | Fix command for contributor                                                                                     |
| ------------------------------------------------------ | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `❌ docs/site/catalog/ is out of date, run: bake lint` | Generated docs not committed                           | `bake lint`                                                                                                     |
| `❌ docs/site/problems/ is out of date`                | Generated docs not committed                           | `bake lint`                                                                                                     |
| `files were modified by this hook` (`nb-to-py` hook)   | Committed `playground.ipynb`                           | `bake lint`, then commit converted `leetcode/<problem>/playground.py`; the `.ipynb` must not stay in the commit |
| `files were modified by this hook` (`lint` hook)       | Generated docs / prettier drift                        | `bake lint`, then commit all modified files                                                                     |
| `sort_tags` / `check_tag_problems` fails               | Tag lists out of sync                                  | `bake lint`                                                                                                     |
| ruff format / ty / deptry failures                     | Lint violations in solution code                       | `bake lint` (auto-fixes format); hand-fix ty findings                                                           |
| `check-consistency` drift                              | Committed `leetcode/` files diverge from JSON template | `bake check-consistency` — see consistency-fix skill. Never `p-gen -f` on a solved problem                      |
| test case count below threshold                        | Too few test cases                                     | `bake check-test-cases -t <n>` locally to see offenders                                                         |

**Most common single fix:** contributor added a new problem but skipped generated files. `bake lint` regenerates `docs/site/catalog/`, `docs/site/problems/`, runs prettier/ruff/ty, and the `nb-to-py` pre-commit hook converts `playground.ipynb` → `playground.py`. Both `pre-commit` and `test-reproducibility` jobs then pass.

## Repo Conventions to Check in a New-Problem PR

- `leetcode/<problem>/` needs: `README.md`, `solution.py`, `test_solution.py`, `helpers.py`, `playground.py` (converted, not `.ipynb`), `__init__.py`
- JSON template at `src/leetcode_py/cli/resources/leetcode/json/problems/<problem>.json` is the source of truth
- `docs/site/problems/<slug>.mdx` is generated — contributors should not hand-write it, but it must be committed

## Reply Template

- Open with `@<login>` + exactly one short thanks.
- Match opener's language (Chinese or English).
- Name the failed jobs, give the root cause in one sentence, give the exact fix command in a code block.
- Name the files to commit (usually `docs/site/catalog/`, `docs/site/problems/`, `leetcode/<problem>/playground.py`).
- Close with a concrete next step (push, then merge once green).
- Short paragraphs, no bullet ceremony, no closing thanks stacks.
- Comment as maintainer, not as AI; no attribution footer on PR comments.

## Pushing Fixes Directly

If `maintainerCanModify` is true and the user prefers speed over a contributor round-trip:

1. Fetch the PR branch, run `bake lint` + `uv run pre-commit run --all-files`.
2. Commit generated files, push to the PR branch.
3. Verify `gh pr checks` goes green, then merge.

Confirm with the user before pushing to someone else's branch.

## Clobber Warning

Never run `bake p-gen -f` on an already-solved problem to "fix" drift — it clobbers `solution.py` back to stubs. See consistency-fix skill and the stub-poisoning history in the skill-suggestions log.
