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
from helpers import assert_kth_largest_number, run_kth_largest_number
from solution import Solution

# %%
# Example test case
nums = ["3", "6", "7", "10"]
k = 4
expected = "3"

# %%
result = run_kth_largest_number(Solution, nums, k)
result

# %%
assert_kth_largest_number(result, expected)
