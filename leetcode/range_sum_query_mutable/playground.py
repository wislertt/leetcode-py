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
from helpers import assert_num_array, run_num_array
from solution import NumArray

# %%
# Example test case
operations = ["NumArray", "sum_range", "update", "sum_range"]
inputs = [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
expected = [None, 9, None, 8]

# %%
result, num_array = run_num_array(NumArray, operations, inputs)
print(result)
num_array

# %%
assert_num_array(result, expected)
