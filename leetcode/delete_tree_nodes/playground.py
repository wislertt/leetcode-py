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
from helpers import assert_delete_tree_nodes, run_delete_tree_nodes
from solution import Solution

# %%
# Example test case
nodes = 7
parent = [-1, 0, 0, 1, 2, 2, 2]
value = [1, -2, 4, 0, -2, -1, -1]
expected = 2

# %%
result = run_delete_tree_nodes(Solution, nodes, parent, value)
result

# %%
assert_delete_tree_nodes(result, expected)
