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
from helpers import assert_max_subarray_length, run_max_subarray_length
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 1, 2, 3, 1, 2]
k = 2
expected = 6

# %%
result = run_max_subarray_length(Solution, nums, k)
result

# %%
assert_max_subarray_length(result, expected)
