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
from helpers import assert_largest_divisible_subset, run_largest_divisible_subset
from solution import Solution

# %%
# Example test case
nums = [1, 2, 4, 8]
expected = [1, 2, 4, 8]

# %%
result = run_largest_divisible_subset(Solution, nums)
result

# %%
assert_largest_divisible_subset(result, expected)
