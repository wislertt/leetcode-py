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
from helpers import assert_zigzag_iterator, run_zigzag_iterator
from solution import ZigzagIterator

# %%
# Example test case
operations = ["ZigzagIterator", "next", "next", "next", "next", "next", "next", "has_next"]
inputs = [[[1, 2], [3, 4, 5, 6]], [], [], [], [], [], [], []]
expected = [None, 1, 3, 2, 4, 5, 6, False]

# %%
result, iterator = run_zigzag_iterator(ZigzagIterator, operations, inputs)
print(result)
iterator

# %%
assert_zigzag_iterator(result, expected)
