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
from helpers import assert_hash_set, run_hash_set
from solution import MyHashSet

# %%
# Example test case
operations = [
    "MyHashSet",
    "add",
    "add",
    "contains",
    "contains",
    "add",
    "contains",
    "remove",
    "contains",
]
inputs = [[], [1], [2], [1], [3], [2], [2], [2], [2]]
expected = [None, None, None, True, False, None, True, None, False]

# %%
result, hash_set = run_hash_set(MyHashSet, operations, inputs)
print(result)
hash_set

# %%
assert_hash_set(result, expected)
