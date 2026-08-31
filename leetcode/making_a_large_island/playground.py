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
from helpers import assert_largest_island, run_largest_island
from solution import Solution

# %%
# Example test case
grid = [[1, 0], [0, 1]]
expected = 3

# %%
result = run_largest_island(Solution, grid)
result

# %%
assert_largest_island(result, expected)
