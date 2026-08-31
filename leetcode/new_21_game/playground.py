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
from helpers import assert_new21_game, run_new21_game
from solution import Solution

# %%
# Example test case
n = 10
k = 1
max_pts = 10
expected = 1.0

# %%
result = run_new21_game(Solution, n, k, max_pts)
result

# %%
assert_new21_game(result, expected)
