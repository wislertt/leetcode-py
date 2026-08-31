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
from helpers import assert_sum_subarray_mins, run_sum_subarray_mins
from solution import Solution

# %%
# Example test case
arr = [3, 1, 2, 4]
expected = 17

# %%
result = run_sum_subarray_mins(Solution, arr)
result

# %%
assert_sum_subarray_mins(result, expected)
