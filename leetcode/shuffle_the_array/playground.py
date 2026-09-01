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
from helpers import assert_shuffle, run_shuffle
from solution import Solution

# %%
# Example test case
nums = [2, 5, 1, 3, 4, 7]
n = 3
expected = [2, 3, 5, 4, 1, 7]

# %%
result = run_shuffle(Solution, nums, n)
result

# %%
assert_shuffle(result, expected)
