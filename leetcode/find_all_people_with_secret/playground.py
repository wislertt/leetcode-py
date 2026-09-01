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
from helpers import assert_find_all_people, run_find_all_people
from solution import Solution

# %%
# Example test case
n = 6
meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
first_person = 1
expected = [0, 1, 2, 3, 5]

# %%
result = run_find_all_people(Solution, n, meetings, first_person)
result

# %%
assert_find_all_people(result, expected)
