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
from helpers import assert_validate_binary_tree_nodes, run_validate_binary_tree_nodes
from solution import Solution

# %%
# Example test case
n = 4
left_child = [1, -1, 3, -1]
right_child = [2, -1, -1, -1]
expected = True

# %%
result = run_validate_binary_tree_nodes(Solution, n, left_child, right_child)
result

# %%
assert_validate_binary_tree_nodes(result, expected)
