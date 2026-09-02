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
from helpers import assert_peeking_iterator, run_peeking_iterator
from solution import PeekingIterator

# %%
# Example test case
operations = ["PeekingIterator", "next", "peek", "next", "next", "has_next"]
inputs = [[[1, 2, 3]], [], [], [], [], []]
expected = [None, 1, 2, 2, 3, False]

# %%
result, iterator = run_peeking_iterator(PeekingIterator, operations, inputs)
print(result)
iterator

# %%
assert_peeking_iterator(result, expected)
