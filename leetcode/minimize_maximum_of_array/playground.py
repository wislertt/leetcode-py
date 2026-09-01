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
from helpers import assert_minimize_array_value, run_minimize_array_value
from solution import Solution

# %%
# Example test case
nums = [3, 7, 1, 6]
expected = 5

# %%
result = run_minimize_array_value(Solution, nums)
result

# %%
assert_minimize_array_value(result, expected)
