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
from helpers import assert_operations_on_tree, run_operations_on_tree
from solution import LockingTree

# %%
# Example test case
operations = ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
inputs = [[-1, 0, 0, 1, 1, 2, 2], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
expected = [None, True, False, True, True, True, False]

# %%
result, tree = run_operations_on_tree(LockingTree, operations, inputs)
print(result)
tree

# %%
assert_operations_on_tree(result, expected)
