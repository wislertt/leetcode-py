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
from helpers import assert_flatten_nested_list_iterator, run_flatten_nested_list_iterator
from solution import NestedIterator

# %%
# Example test case
nested_list = [[1, 1], 2, [1, 1]]
expected = [1, 1, 2, 1, 1]

# %%
result = run_flatten_nested_list_iterator(NestedIterator, nested_list)
result

# %%
assert_flatten_nested_list_iterator(result, expected)
