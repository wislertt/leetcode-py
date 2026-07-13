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
from helpers import assert_remove_leaf_nodes, run_remove_leaf_nodes
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, 2, None, 2, 4]
target = 2
expected_list: list[int | None] = [1, None, 3, None, 4]

# %%
result = run_remove_leaf_nodes(Solution, root_list, target)
result

# %%
assert_remove_leaf_nodes(result, expected_list)
