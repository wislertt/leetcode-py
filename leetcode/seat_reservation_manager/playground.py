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
from helpers import assert_seat_reservation_manager, run_seat_reservation_manager
from solution import SeatManager

# %%
# Example test case
operations = [
    "SeatManager",
    "reserve",
    "reserve",
    "unreserve",
    "reserve",
    "reserve",
    "reserve",
    "reserve",
    "unreserve",
]
inputs = [[5], [], [], [2], [], [], [], [], [5]]
expected = [None, 1, 2, None, 2, 3, 4, 5, None]

# %%
result, manager = run_seat_reservation_manager(SeatManager, operations, inputs)
print(result)
manager

# %%
assert_seat_reservation_manager(result, expected)
