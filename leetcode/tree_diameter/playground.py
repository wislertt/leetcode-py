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
from helpers import assert_tree_diameter, run_tree_diameter
from solution import Solution

# %%
# Example test case
edges: list[list[int]] = [[0, 1], [0, 2]]
expected = 2

# %%
result = run_tree_diameter(Solution, edges)
result

# %%
assert_tree_diameter(result, expected)
