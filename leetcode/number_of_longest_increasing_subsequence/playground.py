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
from helpers import assert_find_number_of_lis, run_find_number_of_lis
from solution import Solution

# %%
# Example test case
nums = [1, 3, 5, 4, 7]
expected = 2

# %%
result = run_find_number_of_lis(Solution, nums)
result

# %%
assert_find_number_of_lis(result, expected)
