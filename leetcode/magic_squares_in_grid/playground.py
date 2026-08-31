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
from helpers import assert_num_magic_squares_inside, run_num_magic_squares_inside
from solution import Solution

# %%
# Example test case
grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
expected = 1

# %%
result = run_num_magic_squares_inside(Solution, grid)
result

# %%
assert_num_magic_squares_inside(result, expected)
