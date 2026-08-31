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
from helpers import assert_num_submatrix_sum_target, run_num_submatrix_sum_target
from solution import Solution

# %%
# Example test case
matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
target = 0
expected = 4

# %%
result = run_num_submatrix_sum_target(Solution, matrix, target)
result

# %%
assert_num_submatrix_sum_target(result, expected)
