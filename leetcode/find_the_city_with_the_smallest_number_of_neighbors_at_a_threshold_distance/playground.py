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
from helpers import assert_find_the_city, run_find_the_city
from solution import Solution

# %%
# Example test case
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distance_threshold = 4
expected = 3

# %%
result = run_find_the_city(Solution, n, edges, distance_threshold)
result

# %%
assert_find_the_city(result, expected)
