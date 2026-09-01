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
from helpers import assert_minimum_size, run_minimum_size
from solution import Solution

# %%
# Example test case
nums = [9]
max_operations = 2
expected = 3

# %%
result = run_minimum_size(Solution, nums, max_operations)
result

# %%
assert_minimum_size(result, expected)
