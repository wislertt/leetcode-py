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
from helpers import assert_get_concatenation, run_get_concatenation
from solution import Solution

# %%
# Example test case
nums = [1, 2, 1]
expected = [1, 2, 1, 1, 2, 1]

# %%
result = run_get_concatenation(Solution, nums)
result

# %%
assert_get_concatenation(result, expected)
