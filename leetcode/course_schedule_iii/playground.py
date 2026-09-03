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
from helpers import assert_schedule_course, run_schedule_course
from solution import Solution

# %%
# Example test case
courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
expected = 3

# %%
result = run_schedule_course(Solution, courses)
result

# %%
assert_schedule_course(result, expected)
