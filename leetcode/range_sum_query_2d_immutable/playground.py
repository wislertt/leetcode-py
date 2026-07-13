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
from helpers import assert_num_matrix, run_num_matrix
from solution import NumMatrix

# %%
# Example test case
operations = ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
inputs = [
    [[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],
    [2, 1, 4, 3],
    [1, 1, 2, 2],
    [1, 2, 2, 4],
]
expected = [None, 8, 11, 12]

# %%
result, num_matrix = run_num_matrix(NumMatrix, operations, inputs)
print(result)
num_matrix

# %%
assert_num_matrix(result, expected)
