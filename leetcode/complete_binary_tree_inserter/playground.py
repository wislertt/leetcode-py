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
from helpers import assert_complete_binary_tree_inserter, run_complete_binary_tree_inserter
from solution import CBTInserter

# %%
# Example test case
operations = ["CBTInserter", "insert", "insert", "get_root"]
inputs = [[1, 2], [3], [4], []]
expected: list[int | list[int | None] | None] = [None, 1, 2, [1, 2, 3, 4]]

# %%
result, inserter = run_complete_binary_tree_inserter(CBTInserter, operations, inputs)
print(result)
inserter

# %%
assert_complete_binary_tree_inserter(result, expected)
