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
from helpers import assert_shortest_alternating_paths, run_shortest_alternating_paths
from solution import Solution

# %%
# Example test case
n = 3
red_edges = [[0, 1], [1, 2]]
blue_edges = []
expected = [0, 1, -1]

# %%
result = run_shortest_alternating_paths(Solution, n, red_edges, blue_edges)
result

# %%
assert_shortest_alternating_paths(result, expected)
