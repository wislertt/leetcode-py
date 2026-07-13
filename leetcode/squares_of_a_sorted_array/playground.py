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
from helpers import assert_sorted_squares, run_sorted_squares
from solution import Solution

# %%
# Example test case
nums = [-4, -1, 0, 3, 10]
expected = [0, 1, 9, 16, 100]

# %%
result = run_sorted_squares(Solution, nums)
result

# %%
assert_sorted_squares(result, expected)
