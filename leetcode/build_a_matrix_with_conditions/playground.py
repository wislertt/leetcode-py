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
from helpers import assert_build_matrix, run_build_matrix
from solution import Solution

# %%
# Example test case
k = 3
row_conditions = [[1, 2], [3, 2]]
col_conditions = [[2, 1], [3, 2]]
valid = True

# %%
result = run_build_matrix(Solution, k, row_conditions, col_conditions)
result

# %%
assert_build_matrix(result, k, row_conditions, col_conditions, valid)
