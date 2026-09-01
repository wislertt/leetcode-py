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
from helpers import assert_find_smallest_set_of_vertices, run_find_smallest_set_of_vertices
from solution import Solution

# %%
# Example test case
n = 6
edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
expected = [0, 3]

# %%
result = run_find_smallest_set_of_vertices(Solution, n, edges)
result

# %%
assert_find_smallest_set_of_vertices(result, expected)
