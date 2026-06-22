# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_find_redundant_connection, run_find_redundant_connection
from solution import Solution

# %%
# Example test case
edges = [[1, 2], [1, 3], [2, 3]]
expected = [2, 3]

# %%
result = run_find_redundant_connection(Solution, edges)
result

# %%
assert_find_redundant_connection(result, expected)
