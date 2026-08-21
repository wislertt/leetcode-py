---
name: leetcode-py
description: Generates Python LeetCode practice environments and manages a 307-problem catalog with the lcpy CLI. Use when a repository needs coding interview practice scaffolding: generating problem directories (README, solution stub, parametrized pytest suite, helpers, notebook); setting up collections like Blind 75, Grind 75, Grind 169, NeetCode 150, NeetCode 250, or Algo Master 75; testing LeetCode solutions with loguru-logged, parametrized suites; visualizing TreeNode, ListNode, or GraphNode structures; or scraping LeetCode problem data as JSON. Use even if leetcode-py is not named: "set up interview prep repo", "add leetcode problem", "practice grind 75 in python". Do NOT use for submitting to leetcode.com, fetching judge results or contest rankings, or non-LeetCode competitive programming.
license: Apache-2.0
compatibility: Requires Python 3.10+. The lcpy CLI runs in any repo; bake tasks need this repo cloned.
metadata:
  version: "1.0"
  docs: https://leetcode-py.wisl.dev
  repository: https://github.com/wislertt/leetcode-py
---

# leetcode-py

leetcode-py is a Python LeetCode practice environment generator. `lcpy` generates complete problem directories from JSON templates bundled with the package, so a repo never carries hand-written test scaffolding. This repository is itself one such practice environment kept in sync by the same generator.

## Commands

| Command                  | Purpose                                                                  |
| ------------------------ | ------------------------------------------------------------------------ |
| `lcpy gen -n 1`          | Generate the Two Sum directory (README, stub, tests, helpers, notebook). |
| `lcpy gen -t grind-75`   | Generate every problem in a collection.                                  |
| `lcpy list`              | List the 307 bundled problems in a formatted table.                      |
| `lcpy scrape -n 198`     | Fetch a problem's data from LeetCode as JSON.                            |
| `bake p-test -p two_sum` | Run one problem's test suite (this repo only).                           |
| `bake test`              | Run every suite (this repo only).                                        |

One CLI: `lcpy` generates and lists. `bake` tasks exist only inside a clone of this repository.

## Generating problems

```bash
pip install leetcode-py-sdk
# or
uv tool install leetcode-py-sdk
```

```bash
mkdir my-practice && cd my-practice
lcpy gen -t grind-75    # a full practice env, no repo checkout needed
```

`gen` selects problems by number (`-n 1`), slug (`-s two-sum`), collection tag (`-t blind-75`), difficulty (`-d Easy`), or `--all`; repeatable flags accept several values. `-o` sets the output directory and `--force` overwrites existing files. `gen` refuses to clobber without `--force`.

## Problem anatomy

Each problem lands as `leetcode/<problem_name>/` with six files:

- `README.md` - the problem statement
- `solution.py` - implementation with a TODO stub
- `test_solution.py` - parametrized pytest suite, 10+ cases
- `helpers.py` - `run_*` / `assert_*` functions
- `playground.ipynb` - percent-format notebook
- `__init__.py` - empty package file

## Testing

Suites are parametrized; the same cases cover multiple solution classes:

```python
import pytest

from leetcode_py import logged_test

from .helpers import assert_two_sum, run_two_sum
from .solution import Solution


class TestTwoSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 3], 6, [0, 1]),  # duplicate values
            ([-1, -2, -3, -4, -5], -8, [2, 4]),  # all negatives
            ([1, 2], 5, []),  # no answer exists
            ([-1000000000, 1000000000], 0, [0, 1]),  # boundary values
        ],
    )
    def test_two_sum(self, nums: list[int], target: int, expected: list[int]):
        result = run_two_sum(Solution, nums, target)
        assert_two_sum(result, expected)
```

For a second approach next to the first, parametrize over the class instead of copying the suite:

```python
@pytest.mark.parametrize("solution_class", [Solution, SolutionMath])
@pytest.mark.parametrize("input_params, expected", test_cases)
def test_method(self, solution_class, input_params, expected):
    result = run_helper(solution_class, *input_params)
    assert_helper(result, expected)
```

`logged_test` (from `leetcode_py`, also exports `TreeNode`, `ListNode`, `GraphNode`) logs each case and its result. Helpers accept the solution class as their first argument and normalize comparison, so `[1, 0]` passes against expected `[0, 1]` when order does not matter.

## Collections

Six tags ship in the catalog: `grind-75` (75), `grind` (169), `blind-75` (75), `neetcode-150` (154), `neetcode-250` (253), `algo-master-75` (75). Overlap is allowed. `lcpy list -t <tag>` filters, `lcpy gen -t <tag>` generates the whole set.

## Common gotchas

- `lcpy` is the published CLI (`leetcode-py-sdk` on PyPI) and runs in any repo; `bake` tasks need this repo's `bakefile.py`.
- `gen` fails on existing files; add `--force`.
- Problems are snake_case directories (`two_sum`), LeetCode slugs are kebab-case (`two-sum`); `-s` takes the slug, `-p` in `bake p-test` takes the directory name.
- `@logged_test` wraps the test function and must sit directly above `@pytest.mark.parametrize`.

## Machine-readable docs

- Full docs, single file: https://leetcode-py.wisl.dev/llms-full.txt
- Docs index: https://leetcode-py.wisl.dev/llms.txt
- Docs search via MCP: https://leetcode-py.wisl.dev/mcp
- Install this skill into agent context: `npx skills add https://leetcode-py.wisl.dev`
