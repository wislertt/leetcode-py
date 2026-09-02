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
from helpers import assert_minimum_mountain_removals, run_minimum_mountain_removals
from solution import Solution

# %%
# Example test case
nums = [2, 1, 1, 5, 6, 2, 3, 1]
expected = 3

# %%
result = run_minimum_mountain_removals(Solution, nums)
result

# %%
assert_minimum_mountain_removals(result, expected)
