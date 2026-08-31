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
from helpers import assert_max_sub_array_len, run_max_sub_array_len
from solution import Solution

# %%
# Example test case
nums = [1, -1, 5, -2, 3]
k = 3
expected = 4

# %%
result = run_max_sub_array_len(Solution, nums, k)
result

# %%
assert_max_sub_array_len(result, expected)
