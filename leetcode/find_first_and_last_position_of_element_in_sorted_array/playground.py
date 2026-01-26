# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_search_range, run_search_range
from solution import Solution

# %%
# Example test case
nums: list[int] = [5, 7, 7, 8, 8, 10]
target = 8
expected = [3, 4]

# %%
result = run_search_range(Solution, nums, target)
result

# %%
assert_search_range(result, expected)
