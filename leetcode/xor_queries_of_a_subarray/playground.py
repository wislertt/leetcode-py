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
from helpers import assert_xor_queries, run_xor_queries
from solution import Solution

# %%
# Example test case
arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
expected = [2, 7, 14, 8]

# %%
result = run_xor_queries(Solution, arr, queries)
result

# %%
assert_xor_queries(result, expected)
