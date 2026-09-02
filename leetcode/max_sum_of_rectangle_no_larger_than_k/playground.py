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
from helpers import assert_max_sum_submatrix, run_max_sum_submatrix
from solution import Solution

# %%
# Example test case
matrix = [[1, 0, 1], [0, -2, 3]]
k = 2
expected = 2

# %%
result = run_max_sum_submatrix(Solution, matrix, k)
result

# %%
assert_max_sum_submatrix(result, expected)
