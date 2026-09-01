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
from helpers import assert_average_waiting_time, run_average_waiting_time
from solution import Solution

# %%
# Example test case
customers: list[list[int]] = [[1, 2], [2, 5], [4, 3]]
expected = 5.0

# %%
result = run_average_waiting_time(Solution, customers)
result

# %%
assert_average_waiting_time(result, expected)
