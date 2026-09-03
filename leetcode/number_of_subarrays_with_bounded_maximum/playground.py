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
from helpers import assert_num_subarray_bounded_max, run_num_subarray_bounded_max
from solution import Solution

# %%
# Example test case
nums = [2, 1, 4, 3]
left = 2
right = 3
expected = 3

# %%
result = run_num_subarray_bounded_max(Solution, nums, left, right)
result

# %%
assert_num_subarray_bounded_max(result, expected)
