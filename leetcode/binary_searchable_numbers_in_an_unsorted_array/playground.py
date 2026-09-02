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
from helpers import assert_binary_searchable_numbers, run_binary_searchable_numbers
from solution import Solution

# %%
# Example test case
nums = [-1, 5, 2]
expected = 1

# %%
result = run_binary_searchable_numbers(Solution, nums)
result

# %%
assert_binary_searchable_numbers(result, expected)
