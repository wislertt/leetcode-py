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
from helpers import assert_reachable_nodes, run_reachable_nodes
from solution import Solution

# %%
# Example test case
edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2]]
max_moves = 6
n = 3
expected = 13

# %%
result = run_reachable_nodes(Solution, edges, max_moves, n)
result

# %%
assert_reachable_nodes(result, expected)
