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
from helpers import assert_number_of_arithmetic_slices, run_number_of_arithmetic_slices
from solution import Solution

# %%
# Example test case
nums: list[int] = [1, 2, 3, 4]
expected = 3

# %%
result = run_number_of_arithmetic_slices(Solution, nums)
result

# %%
assert_number_of_arithmetic_slices(result, expected)
