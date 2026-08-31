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
arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
expected = 3

# %%
result = run_num_of_subarrays(Solution, arr, k, threshold)
result

# %%
assert_num_of_subarrays(result, expected)
