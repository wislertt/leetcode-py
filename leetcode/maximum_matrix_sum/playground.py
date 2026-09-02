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
from helpers import assert_max_matrix_sum, run_max_matrix_sum
from solution import Solution

# %%
# Example test case
matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
expected = 16

# %%
result = run_max_matrix_sum(Solution, matrix)
result

# %%
assert_max_matrix_sum(result, expected)
