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
from helpers import assert_design_tic_tac_toe, run_design_tic_tac_toe
from solution import TicTacToe

# %%
# Example test case
operations = ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
inputs = [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
expected = [None, 0, 0, 0, 0, 0, 0, 1]

# %%
result, game = run_design_tic_tac_toe(TicTacToe, operations, inputs)
print(result)
game

# %%
assert_design_tic_tac_toe(result, expected)
