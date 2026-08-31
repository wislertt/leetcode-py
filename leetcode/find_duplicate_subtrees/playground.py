# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_find_duplicate_subtrees, run_find_duplicate_subtrees
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [2, 1, 1]
expected: list[list[int | None]] = [[1]]

# %%
result = run_find_duplicate_subtrees(Solution, root_list)
result

# %%
assert_find_duplicate_subtrees(result, expected)
