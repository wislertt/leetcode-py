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
from helpers import assert_divide_array_into_equal_pairs, run_divide_array_into_equal_pairs
from solution import Solution

# %%
# Example test case
nums = [3, 2, 3, 2, 2, 2]
expected = True

# %%
result = run_divide_array_into_equal_pairs(Solution, nums)
result

# %%
assert_divide_array_into_equal_pairs(result, expected)
