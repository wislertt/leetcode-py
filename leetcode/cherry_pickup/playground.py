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
from helpers import assert_cherry_pickup, run_cherry_pickup
from solution import Solution

# %%
# Example test case
grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
expected = 5

# %%
result = run_cherry_pickup(Solution, grid)
result

# %%
assert_cherry_pickup(result, expected)
