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
from helpers import assert_clean_room, run_clean_room
from solution import Solution

# %%
# Example test case
room = [[1, 1], [1, 0]]
row = 0
col = 0
expected = 3

# %%
result = run_clean_room(Solution, room, row, col)
result

# %%
assert_clean_room(result, expected)
