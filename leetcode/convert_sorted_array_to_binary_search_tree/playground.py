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
from helpers import assert_sorted_array_to_bst, run_sorted_array_to_bst
from solution import Solution

# %%
# Example test case
nums = [-10, -3, 0, 5, 9]

# %%
result = run_sorted_array_to_bst(Solution, nums)
result.to_list() if result else []

# %%
assert_sorted_array_to_bst(result, nums)
