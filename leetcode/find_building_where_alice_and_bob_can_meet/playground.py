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
from helpers import assert_leftmost_building_queries, run_leftmost_building_queries
from solution import Solution

# %%
# Example test case
heights = [6, 4, 8, 5, 2, 7]
queries = [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
expected = [2, 5, -1, 5, 2]

# %%
result = run_leftmost_building_queries(Solution, heights, queries)
result

# %%
assert_leftmost_building_queries(result, expected)
