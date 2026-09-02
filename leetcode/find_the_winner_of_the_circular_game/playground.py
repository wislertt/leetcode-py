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
from helpers import assert_find_the_winner, run_find_the_winner
from solution import Solution

# %%
# Example test case
n = 5
k = 2
expected = 3

# %%
result = run_find_the_winner(Solution, n, k)
result

# %%
assert_find_the_winner(result, expected)
