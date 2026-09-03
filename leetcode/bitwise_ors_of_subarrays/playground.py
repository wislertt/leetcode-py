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
from helpers import assert_subarray_bitwise_ors, run_subarray_bitwise_ors
from solution import Solution

# %%
# Example test case
arr = [1, 1, 2]
expected = 3

# %%
result = run_subarray_bitwise_ors(Solution, arr)
result

# %%
assert_subarray_bitwise_ors(result, expected)
