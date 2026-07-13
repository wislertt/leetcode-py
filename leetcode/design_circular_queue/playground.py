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
from helpers import assert_circular_queue, run_circular_queue
from solution import MyCircularQueue

# %%
# Example test case
operations = [
    "MyCircularQueue",
    "en_queue",
    "en_queue",
    "en_queue",
    "en_queue",
    "rear",
    "is_full",
    "de_queue",
    "en_queue",
    "rear",
]
inputs = [[3], [1], [2], [3], [4], [], [], [], [4], []]
expected = [None, True, True, True, False, 3, True, True, True, 4]

# %%
result, queue = run_circular_queue(MyCircularQueue, operations, inputs)
print(result)
queue

# %%
assert_circular_queue(result, expected)
