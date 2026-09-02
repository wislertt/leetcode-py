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
from helpers import assert_max_num_edges_to_remove, run_max_num_edges_to_remove
from solution import Solution

# %%
# Example test case
n = 4
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
expected = 2

# %%
result = run_max_num_edges_to_remove(Solution, n, edges)
result

# %%
assert_max_num_edges_to_remove(result, expected)
