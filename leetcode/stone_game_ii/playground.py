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
from helpers import assert_stone_game_ii, run_stone_game_ii
from solution import Solution

# %%
# Example test case
piles = [2, 7, 9, 4, 4]
expected = 10

# %%
result = run_stone_game_ii(Solution, piles)
result

# %%
assert_stone_game_ii(result, expected)
