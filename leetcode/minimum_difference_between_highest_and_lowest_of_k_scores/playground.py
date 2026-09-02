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
from helpers import assert_minimum_difference, run_minimum_difference
from solution import Solution

# %%
# Example test case
nums = [9, 4, 1, 7]
k = 2
expected = 2

# %%
result = run_minimum_difference(Solution, nums, k)
result

# %%
assert_minimum_difference(result, expected)
