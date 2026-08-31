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
from helpers import assert_candy_crush, run_candy_crush
from solution import Solution

# %%
# Example test case
board = [[1, 3, 5, 5, 2], [3, 4, 3, 3, 1], [3, 2, 4, 5, 2], [2, 4, 4, 5, 5], [1, 4, 4, 1, 1]]
expected = [[1, 3, 0, 0, 0], [3, 4, 0, 5, 2], [3, 2, 0, 3, 1], [2, 4, 0, 5, 2], [1, 4, 3, 1, 1]]

# %%
result = run_candy_crush(Solution, board)
result

# %%
assert_candy_crush(result, expected)
