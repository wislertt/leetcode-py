# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_my_calendar, run_my_calendar
from solution import MyCalendar

# %%
# Example test case
bookings = [(10, 20), (15, 25), (20, 30)]
expected = [True, False, True]

# %%
result = run_my_calendar(MyCalendar, bookings)
result

# %%
assert_my_calendar(result, expected)
