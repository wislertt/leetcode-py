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
from helpers import assert_assign_bikes, run_assign_bikes
from solution import Solution

# %%
# Example test case
workers = [[0, 0], [2, 1]]
bikes = [[1, 2], [3, 3]]
expected = [1, 0]

# %%
result = run_assign_bikes(Solution, workers, bikes)
result

# %%
assert_assign_bikes(result, expected)
