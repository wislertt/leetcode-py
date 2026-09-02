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
from helpers import assert_string_iterator, run_string_iterator
from solution import StringIterator

# %%
# Example test case
operations = ["StringIterator", "next", "next", "has_next"]
inputs = [["L1e2t1C1o1d1e1"], [], [], []]
expected = [None, "L", "e", True]

# %%
result, iterator = run_string_iterator(StringIterator, operations, inputs)
print(result)
iterator

# %%
assert_string_iterator(result, expected)
