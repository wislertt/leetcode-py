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
from helpers import assert_largest_submatrix, run_largest_submatrix
from solution import Solution

# %%
# Example test case
matrix = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]
expected = 4

# %%
result = run_largest_submatrix(Solution, matrix)
result

# %%
assert_largest_submatrix(result, expected)
