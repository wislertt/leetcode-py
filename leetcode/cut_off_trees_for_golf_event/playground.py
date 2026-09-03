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
from helpers import assert_cut_off_tree, run_cut_off_tree
from solution import Solution

# %%
# Example test case
forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]
expected = 6

# %%
result = run_cut_off_tree(Solution, forest)
result

# %%
assert_cut_off_tree(result, expected)
