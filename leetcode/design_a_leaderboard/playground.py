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
from helpers import assert_leaderboard, run_leaderboard
from solution import Leaderboard

# %%
# Example test case
operations = [
    "Leaderboard",
    "add_score",
    "add_score",
    "add_score",
    "add_score",
    "add_score",
    "top",
    "reset",
    "reset",
    "add_score",
    "top",
]
inputs = [[], [1, 73], [2, 56], [3, 39], [4, 51], [5, 4], [1], [1], [2], [2, 51], [3]]
expected = [None, None, None, None, None, None, 73, None, None, None, 141]

# %%
result, board = run_leaderboard(Leaderboard, operations, inputs)
print(result)
board

# %%
assert_leaderboard(result, expected)
