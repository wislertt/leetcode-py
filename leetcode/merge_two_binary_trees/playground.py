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
from helpers import assert_merge_trees, run_merge_trees
from solution import Solution

# %%
# Example test case
root1_list: list[int | None] = [1, 3, 2, 5]
root2_list: list[int | None] = [2, 1, 3, None, 4, None, 7]
expected: list[int | None] = [3, 4, 5, 5, 4, None, 7]

# %%
result = run_merge_trees(Solution, root1_list, root2_list)
result

# %%
assert_merge_trees(result, expected)
