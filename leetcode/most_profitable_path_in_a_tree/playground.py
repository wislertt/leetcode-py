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
from helpers import assert_most_profitable_path, run_most_profitable_path
from solution import Solution

# %%
# Example test case
edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
bob = 3
amount = [-2, 4, 2, -4, 6]
expected = 6

# %%
result = run_most_profitable_path(Solution, edges, bob, amount)
result

# %%
assert_most_profitable_path(result, expected)
