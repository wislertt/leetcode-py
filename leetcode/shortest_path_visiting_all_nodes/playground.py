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
from helpers import assert_shortest_path_length, run_shortest_path_length
from solution import Solution

# %%
# Example test case
graph = [[1, 2, 3], [0], [0], [0]]
expected = 4

# %%
result = run_shortest_path_length(Solution, graph)
result

# %%
assert_shortest_path_length(result, expected)
