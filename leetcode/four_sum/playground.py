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
from helpers import assert_four_sum, run_four_sum
from solution import Solution

# %%
# Example test case
nums = [1, 0, -1, 0, -2, 2]
target = 0
expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

# %%
result = run_four_sum(Solution, nums, target)
result

# %%
assert_four_sum(result, expected)
