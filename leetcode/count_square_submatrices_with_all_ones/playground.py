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
from helpers import assert_count_squares, run_count_squares
from solution import Solution

# %%
# Example test case
matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
expected = 15

# %%
result = run_count_squares(Solution, matrix)
result

# %%
assert_count_squares(result, expected)
