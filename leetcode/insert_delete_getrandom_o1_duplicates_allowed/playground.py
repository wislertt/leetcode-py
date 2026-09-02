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
from helpers import assert_randomized_collection_operations, run_randomized_collection_operations
from solution import RandomizedCollection

# %%
# Example test case
operations = [
    "RandomizedCollection",
    "insert",
    "insert",
    "insert",
    "getRandom",
    "remove",
    "getRandom",
]
inputs = [[], [1], [1], [1], [], [1], []]
expected = [None, True, False, False, 1, True, 1]

# %%
result = run_randomized_collection_operations(RandomizedCollection, operations, inputs)
result

# %%
assert_randomized_collection_operations(result, expected)
