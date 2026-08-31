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
from helpers import assert_wiggle_sort, run_wiggle_sort
from solution import Solution

# %%
# Example test case
nums = [3, 5, 2, 1, 6, 4]
expected = [3, 5, 2, 1, 6, 4]

# %%
result = run_wiggle_sort(Solution, nums)
result

# %%
assert_wiggle_sort(result, expected)
