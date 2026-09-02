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
from helpers import assert_get_sum_absolute_differences, run_get_sum_absolute_differences
from solution import Solution

# %%
# Example test case
nums = [2, 3, 5]
expected = [4, 3, 5]

# %%
result = run_get_sum_absolute_differences(Solution, nums)
result

# %%
assert_get_sum_absolute_differences(result, expected)
