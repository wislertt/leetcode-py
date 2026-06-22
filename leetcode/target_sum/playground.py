# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_find_target_sum_ways, run_find_target_sum_ways
from solution import Solution

# %%
# Example test case
nums = [1, 1, 1, 1, 1]
target = 3
expected = 5

# %%
result = run_find_target_sum_ways(Solution, nums, target)
result

# %%
assert_find_target_sum_ways(result, expected)
