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
from helpers import assert_restore_matrix, run_restore_matrix
from solution import Solution

# %%
# Example test case
row_sum = [3, 8]
col_sum = [4, 7]
expected = [[3, 0], [1, 7]]

# %%
result = run_restore_matrix(Solution, row_sum, col_sum)
result

# %%
assert_restore_matrix(result, row_sum, col_sum, expected)
