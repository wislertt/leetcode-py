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
from helpers import assert_find_max_average, run_find_max_average
from solution import Solution

# %%
# Example test case
nums = [1, 12, -5, -6, 50, 3]
k = 4
expected = 12.75

# %%
result = run_find_max_average(Solution, nums, k)
result

# %%
assert_find_max_average(result, expected)
