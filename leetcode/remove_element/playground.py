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
from helpers import assert_remove_element, run_remove_element
from solution import Solution

# %%
# Example test case
nums = [3, 2, 2, 3]
val = 3
expected = (2, [2, 2])

# %%
result = run_remove_element(Solution, nums, val)
result

# %%
assert_remove_element(result, expected)
