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
from helpers import assert_min_sub_array_len, run_min_sub_array_len
from solution import Solution

# %%
# Example test case
target = 7
nums = [2, 3, 1, 2, 4, 3]
expected = 2

# %%
result = run_min_sub_array_len(Solution, target, nums)
result

# %%
assert_min_sub_array_len(result, expected)
