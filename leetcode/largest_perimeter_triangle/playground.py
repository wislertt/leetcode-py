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
from helpers import assert_largest_perimeter, run_largest_perimeter
from solution import Solution

# %%
# Example test case
nums = [2, 1, 2]
expected = 5

# %%
result = run_largest_perimeter(Solution, nums)
result

# %%
assert_largest_perimeter(result, expected)
