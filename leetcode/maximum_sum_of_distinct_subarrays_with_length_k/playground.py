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
from helpers import assert_maximum_subarray_sum, run_maximum_subarray_sum
from solution import Solution

# %%
# Example test case
nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
expected = 15

# %%
result = run_maximum_subarray_sum(Solution, nums, k)
result

# %%
assert_maximum_subarray_sum(result, expected)
