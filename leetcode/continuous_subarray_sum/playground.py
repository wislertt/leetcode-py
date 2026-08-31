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
from helpers import assert_check_subarray_sum, run_check_subarray_sum
from solution import Solution

# %%
# Example test case
nums = [23, 2, 4, 6, 7]
k = 6
expected = True

# %%
result = run_check_subarray_sum(Solution, nums, k)
result

# %%
assert_check_subarray_sum(result, expected)
