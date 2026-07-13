# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_shortest_path_binary_matrix, run_shortest_path_binary_matrix
from solution import Solution

# %%
# Example test case
grid = [[0, 1], [1, 0]]
expected = 2

# %%
result = run_shortest_path_binary_matrix(Solution, grid)
result

# %%
assert_shortest_path_binary_matrix(result, expected)
