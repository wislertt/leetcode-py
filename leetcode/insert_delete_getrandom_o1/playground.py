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
from helpers import assert_randomized_set_operations, run_randomized_set_operations
from solution import RandomizedSet

# %%
# Example test case
operations = ["RandomizedSet", "insert", "getRandom"]
inputs = [[], [5], []]
expected = [None, True, 5]

# %%
result = run_randomized_set_operations(RandomizedSet, operations, inputs)
result

# %%
assert_randomized_set_operations(result, expected)
