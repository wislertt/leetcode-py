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
from helpers import assert_shift_grid, run_shift_grid
from solution import Solution

# %%
# Example test case
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
expected = [[9, 1, 2], [3, 4, 5], [6, 7, 8]]

# %%
result = run_shift_grid(Solution, grid, k)
result

# %%
assert_shift_grid(result, expected)
