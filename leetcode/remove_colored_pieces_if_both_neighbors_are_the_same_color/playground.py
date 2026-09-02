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
from helpers import assert_winner_of_game, run_winner_of_game
from solution import Solution

# %%
# Example test case
colors = "AAABABB"
expected = True

# %%
result = run_winner_of_game(Solution, colors)
result

# %%
assert_winner_of_game(result, expected)
