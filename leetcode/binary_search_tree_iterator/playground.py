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
from helpers import assert_binary_search_tree_iterator, run_binary_search_tree_iterator
from solution import BSTIterator

# %%
# Example test case
root_list: list[int | None] = [7, 3, 15, None, None, 9, 20]
operations = [
    "next",
    "next",
    "has_next",
    "next",
    "has_next",
    "next",
    "has_next",
    "next",
    "has_next",
]
expected: list[int | bool | None] = [None, 3, 7, True, 9, True, 15, True, 20, False]

# %%
result, iterator = run_binary_search_tree_iterator(BSTIterator, root_list, operations)
print(result)
iterator

# %%
assert_binary_search_tree_iterator(result, expected)
