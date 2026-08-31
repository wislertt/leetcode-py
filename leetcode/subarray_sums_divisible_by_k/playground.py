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
from helpers import assert_subarrays_div_by_k, run_subarrays_div_by_k
from solution import Solution

# %%
# Example test case
nums = [4, 5, 0, -2, -3, 1]
k = 5
expected = 7

# %%
result = run_subarrays_div_by_k(Solution, nums, k)
result

# %%
assert_subarrays_div_by_k(result, expected)
