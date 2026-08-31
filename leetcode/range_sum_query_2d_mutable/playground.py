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
from helpers import assert_range_sum_query_2d_mutable, run_range_sum_query_2d_mutable
from solution import NumMatrix

# %%
# Example test case
operations = ["NumMatrix", "sum_region", "update", "sum_region"]
inputs = [
    [[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],
    [2, 1, 4, 3],
    [3, 2, 2],
    [2, 1, 4, 3],
]
expected = [None, 8, None, 10]

# %%
result, matrix_obj = run_range_sum_query_2d_mutable(NumMatrix, operations, inputs)
print(result)
matrix_obj

# %%
assert_range_sum_query_2d_mutable(result, expected)
