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
from helpers import assert_rearrange_array, run_rearrange_array
from solution import Solution

# %%
# Example test case
nums = [3, 1, -2, -5, 2, -4]
expected = [3, -2, 1, -5, 2, -4]

# %%
result = run_rearrange_array(Solution, nums, expected)
result

# %%
assert_rearrange_array(result, expected)
