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
from helpers import assert_pancake_sort, run_pancake_sort
from solution import Solution

# %%
# Example test case
arr = [3, 2, 4, 1]
expected = [1, 2, 3, 4]

# %%
result = run_pancake_sort(Solution, arr)
result

# %%
assert_pancake_sort(result, arr, expected)
