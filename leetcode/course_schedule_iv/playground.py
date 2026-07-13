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
from helpers import assert_check_if_prerequisite, run_check_if_prerequisite
from solution import Solution

# %%
# Example test case
num_courses = 2
prerequisites = [[1, 0]]
queries = [[0, 1], [1, 0]]
expected = [False, True]

# %%
result = run_check_if_prerequisite(Solution, num_courses, prerequisites, queries)
result

# %%
assert_check_if_prerequisite(result, expected)
