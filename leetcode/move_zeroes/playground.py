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
from helpers import assert_move_zeroes, run_move_zeroes
from solution import Solution

# %%
# Example test case
nums = [0, 1, 0, 3, 12]
expected = [1, 3, 12, 0, 0]

# %%
result = run_move_zeroes(Solution, nums)
result

# %%
assert_move_zeroes(result, expected)
