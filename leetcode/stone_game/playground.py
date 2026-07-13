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
from helpers import assert_stone_game, run_stone_game
from solution import Solution

# %%
# Example test case
piles = [5, 3, 4, 5]
expected = True

# %%
result = run_stone_game(Solution, piles)
result

# %%
assert_stone_game(result, expected)
