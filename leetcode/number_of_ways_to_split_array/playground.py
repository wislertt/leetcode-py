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
from helpers import assert_ways_to_split_array, run_ways_to_split_array
from solution import Solution

# %%
# Example test case
nums = [10, 4, -8, 7]
expected = 2

# %%
result = run_ways_to_split_array(Solution, nums)
result

# %%
assert_ways_to_split_array(result, expected)
