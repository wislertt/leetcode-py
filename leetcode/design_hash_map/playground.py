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
from helpers import assert_hash_map, run_hash_map
from solution import MyHashMap

# %%
# Example test case
operations = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
inputs = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
expected = [None, None, None, 1, -1, None, 1, None, -1]

# %%
result, hash_map = run_hash_map(MyHashMap, operations, inputs)
print(result)
hash_map

# %%
assert_hash_map(result, expected)
