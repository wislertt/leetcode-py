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
from helpers import assert_find_least_num_of_unique_ints, run_find_least_num_of_unique_ints
from solution import Solution

# %%
# Example test case
arr = [5, 5, 4]
k = 1
expected = 1

# %%
result = run_find_least_num_of_unique_ints(Solution, arr, k)
result

# %%
assert_find_least_num_of_unique_ints(result, expected)
