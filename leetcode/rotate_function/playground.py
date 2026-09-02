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
from helpers import assert_max_rotate_function, run_max_rotate_function
from solution import Solution

# %%
# Example test case
nums = [4, 3, 2, 6]
expected = 26

# %%
result = run_max_rotate_function(Solution, nums)
result

# %%
assert_max_rotate_function(result, expected)
