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
from helpers import assert_game_of_life, run_game_of_life
from solution import Solution

# %%
# Example test case
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

# %%
result = run_game_of_life(Solution, board)
result

# %%
assert_game_of_life(result, expected)
