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
from helpers import assert_num_of_subarrays, run_num_of_subarrays
from solution import Solution

# %%
# Example test case
arr = [1, 3, 5]
expected = 4

# %%
result = run_num_of_subarrays(Solution, arr)
result

# %%
assert_num_of_subarrays(result, expected)
