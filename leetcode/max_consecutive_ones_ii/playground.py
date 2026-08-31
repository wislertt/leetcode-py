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
from helpers import assert_find_max_ones, run_find_max_ones
from solution import Solution

# %%
# Example test case
nums = [1, 0, 1, 1, 0]
expected = 4

# %%
result = run_find_max_ones(Solution, nums)
result

# %%
assert_find_max_ones(result, expected)
