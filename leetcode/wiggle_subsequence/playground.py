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
from helpers import assert_wiggle_max_length, run_wiggle_max_length
from solution import Solution

# %%
# Example test case
nums: list[int] = [1, 7, 4, 9, 2, 5]
expected = 6

# %%
result = run_wiggle_max_length(Solution, nums)
result

# %%
assert_wiggle_max_length(result, expected)
