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
from helpers import assert_circular_deque, run_circular_deque
from solution import MyCircularDeque

# %%
# Example test case
operations = [
    "MyCircularDeque",
    "insert_last",
    "insert_last",
    "insert_front",
    "insert_front",
    "get_rear",
    "is_full",
    "delete_last",
    "insert_front",
    "get_front",
]
inputs = [[3], [1], [2], [3], [4], [], [], [], [4], []]
expected = [None, True, True, True, False, 2, True, True, True, 4]

# %%
result, deq = run_circular_deque(MyCircularDeque, operations, inputs)
print(result)
deq

# %%
assert_circular_deque(result, expected)
