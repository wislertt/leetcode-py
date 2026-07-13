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
from helpers import assert_combination_sum4, run_combination_sum4
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3]
target = 4
expected = 7

# %%
result = run_combination_sum4(Solution, nums, target)
result

# %%
assert_combination_sum4(result, expected)
