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
from helpers import assert_array_nesting, run_array_nesting
from solution import Solution

# %%
# Example test case
nums = [5, 4, 0, 3, 1, 6, 2]
expected = 4

# %%
result = run_array_nesting(Solution, nums)
result

# %%
assert_array_nesting(result, expected)
