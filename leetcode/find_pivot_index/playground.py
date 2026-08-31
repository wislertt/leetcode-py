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
from helpers import assert_pivot_index, run_pivot_index
from solution import Solution

# %%
# Example test case
nums = [1, 7, 3, 6, 5, 6]
expected = 3

# %%
result = run_pivot_index(Solution, nums)
result

# %%
assert_pivot_index(result, expected)
