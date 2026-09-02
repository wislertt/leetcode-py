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
from helpers import assert_shortest_distance_after_queries, run_shortest_distance_after_queries
from solution import Solution

# %%
# Example test case
n = 5
queries = [[2, 4], [0, 2], [0, 4]]
expected = [3, 2, 1]

# %%
result = run_shortest_distance_after_queries(Solution, n, queries)
result

# %%
assert_shortest_distance_after_queries(result, expected)
