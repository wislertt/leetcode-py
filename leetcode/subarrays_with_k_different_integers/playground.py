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
from helpers import assert_subarrays_with_k_distinct, run_subarrays_with_k_distinct
from solution import Solution

# %%
# Example test case
nums = [1, 2, 1, 2, 3]
k = 2
expected = 7

# %%
result = run_subarrays_with_k_distinct(Solution, nums, k)
result

# %%
assert_subarrays_with_k_distinct(result, expected)
