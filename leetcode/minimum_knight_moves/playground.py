# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_min_knight_moves, run_min_knight_moves
from solution import Solution

# %%
# Example test case
x = 2
y = 1
expected = 1

# %%
result = run_min_knight_moves(Solution, x, y)
result

# %%
assert_min_knight_moves(result, expected)
