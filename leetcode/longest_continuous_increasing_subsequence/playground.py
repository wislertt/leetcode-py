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
from helpers import assert_find_length_of_lcis, run_find_length_of_lcis
from solution import Solution

# %%
# Example test case
nums = [1, 3, 5, 4, 7]
expected = 3

# %%
result = run_find_length_of_lcis(Solution, nums)
result

# %%
assert_find_length_of_lcis(result, expected)
