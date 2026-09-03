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
from helpers import assert_max_vacation_days, run_max_vacation_days
from solution import Solution

# %%
# Example test case
flights = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
days = [[1, 3, 1], [6, 0, 3], [3, 3, 3]]
expected = 12

# %%
result = run_max_vacation_days(Solution, flights, days)
result

# %%
assert_max_vacation_days(result, expected)
