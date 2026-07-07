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
from helpers import assert_three_sum_closest, run_three_sum_closest
from solution import Solution

# %%
# Example test case
nums = [-1, 2, 1, -4]
target = 1
expected = 2

# %%
result = run_three_sum_closest(Solution, nums, target)
result

# %%
assert_three_sum_closest(result, expected)
