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
from helpers import assert_falling_squares, run_falling_squares
from solution import Solution

# %%
# Example test case
positions = [[1, 2], [2, 3], [6, 1]]
expected = [2, 5, 5]

# %%
result = run_falling_squares(Solution, positions)
result

# %%
assert_falling_squares(result, expected)
