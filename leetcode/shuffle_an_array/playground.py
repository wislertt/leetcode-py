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
from helpers import assert_shuffle_operations, run_shuffle_operations
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3]
operations = ["Solution", "shuffle", "reset", "shuffle"]
expected = [None, [1, 2, 3], None]

# %%
result, obj = run_shuffle_operations(Solution, nums, operations)
print(result)
obj

# %%
assert_shuffle_operations(result, expected, nums)
