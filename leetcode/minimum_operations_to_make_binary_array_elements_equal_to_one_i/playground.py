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
from helpers import assert_min_operations, run_min_operations
from solution import Solution

# %%
# Example test case
nums = [0, 1, 1, 1, 0, 0]
expected = 3

# %%
result = run_min_operations(Solution, nums)
result

# %%
assert_min_operations(result, expected)
