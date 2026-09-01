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
from helpers import assert_apply_operations, run_apply_operations
from solution import Solution

# %%
# Example test case
nums = [1, 2, 2, 1, 1, 0]
expected = [1, 4, 2, 0, 0, 0]

# %%
result = run_apply_operations(Solution, nums)
result

# %%
assert_apply_operations(result, expected)
