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
from helpers import assert_find_subsequences, run_find_subsequences
from solution import Solution

# %%
# Example test case
nums = [4, 6, 7, 7]
expected = [
    [4, 6],
    [4, 6, 7],
    [4, 6, 7, 7],
    [4, 7],
    [4, 7, 7],
    [6, 7],
    [6, 7, 7],
    [7, 7],
]

# %%
result = run_find_subsequences(Solution, nums)
result

# %%
assert_find_subsequences(result, expected)
