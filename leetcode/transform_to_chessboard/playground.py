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
from helpers import assert_moves_to_chessboard, run_moves_to_chessboard
from solution import Solution

# %%
# Example test case
board = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
expected = 2

# %%
result = run_moves_to_chessboard(Solution, board)
result

# %%
assert_moves_to_chessboard(result, expected)
