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
from helpers import assert_min_moves_to_seat, run_min_moves_to_seat
from solution import Solution

# %%
# Example test case
seats = [3, 1, 5]
students = [2, 7, 4]
expected = 4

# %%
result = run_min_moves_to_seat(Solution, seats, students)
result

# %%
assert_min_moves_to_seat(result, expected)
