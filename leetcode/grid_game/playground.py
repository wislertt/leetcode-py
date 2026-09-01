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
from helpers import assert_grid_game, run_grid_game
from solution import Solution

# %%
# Example test case
grid = [[2, 5, 4], [1, 5, 1]]
expected = 4

# %%
result = run_grid_game(Solution, grid)
result

# %%
assert_grid_game(result, expected)
