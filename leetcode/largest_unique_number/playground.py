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
from helpers import assert_largest_unique_number, run_largest_unique_number
from solution import Solution

# %%
# Example test case
nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
expected = 8

# %%
result = run_largest_unique_number(Solution, nums)
result

# %%
assert_largest_unique_number(result, expected)
