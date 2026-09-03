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
from helpers import assert_exam_room, run_exam_room
from solution import ExamRoom

# %%
# Example test case
operations = ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
inputs = [[10], [], [], [], [], [4], []]
expected = [None, 0, 9, 4, 2, None, 5]

# %%
result, room = run_exam_room(ExamRoom, operations, inputs)
print(result)
room

# %%
assert_exam_room(result, expected)
