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
from helpers import assert_missing_element, run_missing_element
from solution import Solution

# %%
# Example test case
nums = [4, 7, 9, 10]
k = 3
expected = 8

# %%
result = run_missing_element(Solution, nums, k)
result

# %%
assert_missing_element(result, expected)
