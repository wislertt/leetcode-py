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
from helpers import assert_employee_free_time, run_employee_free_time
from solution import Solution

# %%
# Example test case
schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
expected = [[3, 4]]

# %%
result = run_employee_free_time(Solution, schedule)
result

# %%
assert_employee_free_time(result, expected)
