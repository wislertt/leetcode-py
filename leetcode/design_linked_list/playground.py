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
from helpers import assert_linked_list_ops, run_linked_list_ops
from solution import MyLinkedList

# %%
# Example test case
operations = [
    "MyLinkedList",
    "add_at_head",
    "add_at_tail",
    "add_at_index",
    "get",
    "delete_at_index",
    "get",
]
inputs = [[], [1], [3], [1, 2], [1], [1], [1]]
expected = [None, None, None, None, 2, None, 3]

# %%
result, linked_list = run_linked_list_ops(MyLinkedList, operations, inputs)
print(result)
linked_list

# %%
assert_linked_list_ops(result, expected)
