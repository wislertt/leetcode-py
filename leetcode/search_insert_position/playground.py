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
from helpers import assert_search_insert, run_search_insert
from solution import Solution

# %%
# Example test case
nums = [1, 3, 5, 6]
target = 5
expected = 2

# %%
result = run_search_insert(Solution, nums, target)
result

# %%
assert_search_insert(result, expected)
