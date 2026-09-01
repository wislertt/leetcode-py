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
from helpers import assert_count_students, run_count_students
from solution import Solution

# %%
# Example test case
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
expected = 0

# %%
result = run_count_students(Solution, students, sandwiches)
result

# %%
assert_count_students(result, expected)
