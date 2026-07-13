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
from helpers import assert_find_in_mountain_array, run_find_in_mountain_array
from solution import Solution

# %%
# Example test case
arr = [1, 2, 3, 4, 5, 3, 1]
target = 3
expected = 2

# %%
result = run_find_in_mountain_array(Solution, arr, target)
result

# %%
assert_find_in_mountain_array(result, expected)
