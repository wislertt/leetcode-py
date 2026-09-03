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
from helpers import assert_knight_probability, run_knight_probability
from solution import Solution

# %%
# Example test case
n = 3
k = 2
row = 0
column = 0
expected = 0.0625

# %%
result = run_knight_probability(Solution, n, k, row, column)
result

# %%
assert_knight_probability(result, expected)
