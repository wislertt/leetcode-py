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
from helpers import assert_rle_iterator, run_rle_iterator
from solution import RLEIterator

# %%
# Example test case
operations = ["RLEIterator", "next", "next", "next", "next"]
inputs = [[3, 8, 0, 9, 2, 5], [2], [1], [1], [2]]
expected = [None, 8, 8, 5, -1]

# %%
result, iterator = run_rle_iterator(RLEIterator, operations, inputs)
print(result)
iterator

# %%
assert_rle_iterator(result, expected)
