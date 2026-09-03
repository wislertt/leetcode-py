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
from helpers import assert_is_toeplitz_matrix, run_is_toeplitz_matrix
from solution import Solution

# %%
# Example test case
matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
expected = True

# %%
result = run_is_toeplitz_matrix(Solution, matrix)
result

# %%
assert_is_toeplitz_matrix(result, expected)
