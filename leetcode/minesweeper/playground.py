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
from helpers import assert_update_board, run_update_board
from solution import Solution

# %%
# Example test case
board = [
    ["E", "E", "E", "E", "E"],
    ["E", "E", "M", "E", "E"],
    ["E", "E", "E", "E", "E"],
    ["E", "E", "E", "E", "E"],
]
click = [3, 0]
expected = [
    ["B", "1", "E", "1", "B"],
    ["B", "1", "M", "1", "B"],
    ["B", "1", "1", "1", "B"],
    ["B", "B", "B", "B", "B"],
]

# %%
result = run_update_board(Solution, board, click)
result

# %%
assert_update_board(result, expected)
