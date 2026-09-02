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
from helpers import assert_number_of_subarrays, run_number_of_subarrays
from solution import Solution

# %%
# Example test case
nums = [1, 1, 2, 1, 1]
k = 3
expected = 2

# %%
result = run_number_of_subarrays(Solution, nums, k)
result

# %%
assert_number_of_subarrays(result, expected)
