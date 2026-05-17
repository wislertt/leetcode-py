# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_subarray_sum, run_subarray_sum
from solution import Solution

# %%
# Example test case
nums = [1, 1, 1]
k = 2
expected = 2

# %%
result = run_subarray_sum(Solution, nums, k)
result

# %%
assert_subarray_sum(result, expected)
