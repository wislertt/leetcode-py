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
from helpers import assert_count_ships, run_count_ships
from solution import Solution

# %%
# Example test case
ships = [[1, 1], [2, 2], [3, 3], [5, 5]]
top_right = [4, 4]
bottom_left = [0, 0]
expected = 3

# %%
result = run_count_ships(Solution, ships, top_right, bottom_left)
result

# %%
assert_count_ships(result, expected)
