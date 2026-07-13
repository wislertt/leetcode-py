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
from helpers import assert_stone_game_iii, run_stone_game_iii
from solution import Solution

# %%
# Example test case
stone_value = [1, 2, 3, 7]
expected = "Bob"

# %%
result = run_stone_game_iii(Solution, stone_value)
result

# %%
assert_stone_game_iii(result, expected)
