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
from helpers import assert_is_majority_element, run_is_majority_element
from solution import Solution

# %%
# Example test case
nums = [2, 4, 5, 5, 5, 5, 5, 6, 6]
target = 5
expected = True

# %%
result = run_is_majority_element(Solution, nums, target)
result

# %%
assert_is_majority_element(result, expected)
