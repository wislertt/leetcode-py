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
grid = [[2, 4], [6, 8]]
x = 2
expected = 4

# %%
result = run_min_operations(Solution, grid, x)
result

# %%
assert_min_operations(result, expected)
