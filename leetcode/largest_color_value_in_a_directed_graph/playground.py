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
from helpers import assert_largest_path_value, run_largest_path_value
from solution import Solution

# %%
# Example test case
colors = "abaca"
edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
expected = 3

# %%
result = run_largest_path_value(Solution, colors, edges)
result

# %%
assert_largest_path_value(result, expected)
