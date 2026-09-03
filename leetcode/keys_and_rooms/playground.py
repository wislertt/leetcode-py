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
from helpers import assert_can_visit_all_rooms, run_can_visit_all_rooms
from solution import Solution

# %%
# Example test case
rooms = [[1], [2], [3], []]
expected = True

# %%
result = run_can_visit_all_rooms(Solution, rooms)
result

# %%
assert_can_visit_all_rooms(result, expected)
