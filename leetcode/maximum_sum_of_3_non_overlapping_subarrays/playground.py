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
from helpers import assert_max_sum_of_three_subarrays, run_max_sum_of_three_subarrays
from solution import Solution

# %%
# Example test case
nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
expected = [0, 3, 5]

# %%
result = run_max_sum_of_three_subarrays(Solution, nums, k)
result

# %%
assert_max_sum_of_three_subarrays(result, expected)
