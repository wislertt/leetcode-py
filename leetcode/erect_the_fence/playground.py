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
from helpers import assert_outer_trees, run_outer_trees
from solution import Solution

# %%
# Example test case
trees = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
expected = [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]

# %%
result = run_outer_trees(Solution, trees)
result

# %%
assert_outer_trees(result, expected)
