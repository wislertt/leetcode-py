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
from helpers import assert_two_sum_less_than_k, run_two_sum_less_than_k
from solution import Solution

# %%
# Example test case
nums = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60
expected = 58

# %%
result = run_two_sum_less_than_k(Solution, nums, k)
result

# %%
assert_two_sum_less_than_k(result, expected)
