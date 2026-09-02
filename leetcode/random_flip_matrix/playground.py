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
from helpers import assert_flip_operations, run_flip_operations
from solution import Solution

# %%
# Example test case
m = 3
n = 1
operations = ["Solution", "flip", "flip", "flip", "reset", "flip"]
expected = [None, None, None, None, None]

# %%
result, obj = run_flip_operations(Solution, m, n, operations)
print(result)
obj

# %%
assert_flip_operations(result, expected, m, n)
