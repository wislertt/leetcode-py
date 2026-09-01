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
from helpers import assert_max_absolute_sum, run_max_absolute_sum
from solution import Solution

# %%
# Example test case
nums = [1, -3, 2, 3, -4]
expected = 5

# %%
result = run_max_absolute_sum(Solution, nums)
result

# %%
assert_max_absolute_sum(result, expected)
