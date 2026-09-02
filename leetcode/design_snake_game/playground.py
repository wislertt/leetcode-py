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
from helpers import assert_design_snake_game, run_design_snake_game
from solution import SnakeGame

# %%
# Example test case
operations = ["SnakeGame", "move", "move", "move", "move", "move", "move"]
inputs = [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
expected = [None, 0, 0, 1, 1, 2, -1]

# %%
result, game = run_design_snake_game(SnakeGame, operations, inputs)
print(result)
game

# %%
assert_design_snake_game(result, expected)
