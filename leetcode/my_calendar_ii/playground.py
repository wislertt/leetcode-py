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
from helpers import assert_calendar_ops, run_calendar_ops
from solution import MyCalendarTwo

# %%
# Example test case
operations = ["MyCalendarTwo", "book", "book", "book"]
inputs = [[], [10, 20], [50, 60], [10, 40]]
expected = [None, True, True, True]

# %%
result, calendar = run_calendar_ops(MyCalendarTwo, operations, inputs)
print(result)
calendar

# %%
assert_calendar_ops(result, expected)
