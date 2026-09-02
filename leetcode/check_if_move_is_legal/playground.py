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
from helpers import assert_check_move, run_check_move
from solution import Solution

# %%
# Example test case
board: list[list[str]] = [
    [".", ".", ".", "B", ".", ".", ".", "."],
    [".", ".", ".", "W", ".", ".", ".", "."],
    [".", ".", ".", "W", ".", ".", ".", "."],
    [".", ".", ".", "W", ".", ".", ".", "."],
    ["W", "B", "B", ".", "W", "W", "W", "B"],
    [".", ".", ".", "B", ".", ".", ".", "."],
    [".", ".", ".", "B", ".", ".", ".", "."],
    [".", ".", ".", "W", ".", ".", ".", "."],
]
r_move = 4
c_move = 3
color = "B"
expected = True

# %%
result = run_check_move(Solution, board, r_move, c_move, color)
result

# %%
assert_check_move(result, expected)
