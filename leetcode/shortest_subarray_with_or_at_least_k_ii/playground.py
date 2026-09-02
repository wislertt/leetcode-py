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
from helpers import assert_minimum_subarray_length, run_minimum_subarray_length
from solution import Solution

# %%
# Example test case
nums = [2, 1, 8]
k = 10
expected = 3

# %%
result = run_minimum_subarray_length(Solution, nums, k)
result

# %%
assert_minimum_subarray_length(result, expected)
