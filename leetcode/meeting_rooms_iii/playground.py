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
from helpers import assert_most_booked, run_most_booked
from solution import Solution

# %%
# Example test case
n = 2
meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
expected = 0

# %%
result = run_most_booked(Solution, n, meetings)
result

# %%
assert_most_booked(result, expected)
