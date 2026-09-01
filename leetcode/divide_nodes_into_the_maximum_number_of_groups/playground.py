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
from helpers import assert_magnificent_sets, run_magnificent_sets
from solution import Solution

# %%
# Example test case
n = 6
edges = [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]
expected = 4

# %%
result = run_magnificent_sets(Solution, n, edges)
result

# %%
assert_magnificent_sets(result, expected)
