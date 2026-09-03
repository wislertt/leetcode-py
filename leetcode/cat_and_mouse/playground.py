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
from helpers import assert_cat_mouse_game, run_cat_mouse_game
from solution import Solution

# %%
# Example test case
graph = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
expected = 0

# %%
result = run_cat_mouse_game(Solution, graph)
result

# %%
assert_cat_mouse_game(result, expected)
