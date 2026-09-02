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
from helpers import assert_minimum_semesters, run_minimum_semesters
from solution import Solution

# %%
# Example test case
n = 3
relations = [[1, 3], [2, 3]]
expected = 2

# %%
result = run_minimum_semesters(Solution, n, relations)
result

# %%
assert_minimum_semesters(result, expected)
