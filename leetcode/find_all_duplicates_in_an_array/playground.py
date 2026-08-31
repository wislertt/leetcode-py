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
from helpers import assert_find_duplicates, run_find_duplicates
from solution import Solution

# %%
# Example test case
nums = [4, 3, 2, 7, 8, 2, 3, 1]
expected = [2, 3]

# %%
result = run_find_duplicates(Solution, nums)
result

# %%
assert_find_duplicates(result, expected)
