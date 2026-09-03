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
from helpers import assert_sum_of_distances_in_tree, run_sum_of_distances_in_tree
from solution import Solution

# %%
# Example test case
n = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
expected = [8, 12, 6, 10, 10, 10]

# %%
result = run_sum_of_distances_in_tree(Solution, n, edges)
result

# %%
assert_sum_of_distances_in_tree(result, expected)
