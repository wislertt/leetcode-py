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
from helpers import assert_single_number, run_single_number
from solution import Solution

# %%
# Example test case
nums = [2, 2, 1]
expected = 1

# %%
result = run_single_number(Solution, nums)
result

# %%
assert_single_number(result, expected)
