# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_single_number, run_single_number
from solution import Solution

# %%
# Example test case
nums = [1, 2, 1, 3, 2, 5]
expected = [3, 5]

# %%
result = run_single_number(Solution, nums)
result

# %%
assert_single_number(result, expected)
