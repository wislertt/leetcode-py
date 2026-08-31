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
from helpers import assert_min_increment_for_unique, run_min_increment_for_unique
from solution import Solution

# %%
# Example test case
nums = [3, 2, 1, 2, 1, 7]
expected = 6

# %%
result = run_min_increment_for_unique(Solution, nums)
result

# %%
assert_min_increment_for_unique(result, expected)
