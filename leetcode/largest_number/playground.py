# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_largest_number, run_largest_number
from solution import Solution

# %%
# Example test case
nums = [3, 30, 34, 5, 9]
expected = "9534330"

# %%
result = run_largest_number(Solution, nums)
result

# %%
assert_largest_number(result, expected)
