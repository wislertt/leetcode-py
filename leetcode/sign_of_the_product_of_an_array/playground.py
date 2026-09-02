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
from helpers import assert_array_sign, run_array_sign
from solution import Solution

# %%
# Example test case
nums = [-1, -2, -3, -4, 3, 2, 1]
expected = 1

# %%
result = run_array_sign(Solution, nums)
result

# %%
assert_array_sign(result, expected)
