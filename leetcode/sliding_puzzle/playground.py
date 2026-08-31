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
from helpers import assert_sliding_puzzle, run_sliding_puzzle
from solution import Solution

# %%
# Example test case
board = [[1, 2, 3], [4, 0, 5]]
expected = 1

# %%
result = run_sliding_puzzle(Solution, board)
result

# %%
assert_sliding_puzzle(result, expected)
