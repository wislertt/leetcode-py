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
from helpers import assert_results_array, run_results_array
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 4, 3, 2, 5]
k = 3
expected = [3, 4, -1, -1, -1]

# %%
result = run_results_array(Solution, nums, k)
result

# %%
assert_results_array(result, expected)
