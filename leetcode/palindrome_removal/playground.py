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
from helpers import assert_minimum_moves, run_minimum_moves
from solution import Solution

# %%
# Example test case
arr = [1, 3, 4, 1, 5]
expected = 3

# %%
result = run_minimum_moves(Solution, arr)
result

# %%
assert_minimum_moves(result, expected)
