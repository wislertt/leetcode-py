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
from helpers import assert_count_battleships, run_count_battleships
from solution import Solution

# %%
# Example test case
board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
expected = 2

# %%
result = run_count_battleships(Solution, board)
result

# %%
assert_count_battleships(result, expected)
