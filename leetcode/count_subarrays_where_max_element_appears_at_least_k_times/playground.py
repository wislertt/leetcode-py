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
from helpers import assert_count_subarrays, run_count_subarrays
from solution import Solution

# %%
# Example test case
nums = [1, 3, 2, 3, 3]
k = 2
expected = 6

# %%
result = run_count_subarrays(Solution, nums, k)
result

# %%
assert_count_subarrays(result, expected)
