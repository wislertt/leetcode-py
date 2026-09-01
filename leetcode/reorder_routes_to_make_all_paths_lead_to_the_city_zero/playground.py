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
from helpers import assert_min_reorder, run_min_reorder
from solution import Solution

# %%
# Example test case
n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
expected = 3

# %%
result = run_min_reorder(Solution, n, connections)
result

# %%
assert_min_reorder(result, expected)
