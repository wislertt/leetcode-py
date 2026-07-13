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
from helpers import assert_max_subarray_sum_circular, run_max_subarray_sum_circular
from solution import Solution

# %%
# Example test case
nums = [5, -3, 5]
expected = 10

# %%
result = run_max_subarray_sum_circular(Solution, nums)
result

# %%
assert_max_subarray_sum_circular(result, expected)
