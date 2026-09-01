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
from helpers import assert_most_points, run_most_points
from solution import Solution

# %%
# Example test case
questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
expected = 5

# %%
result = run_most_points(Solution, questions)
result

# %%
assert_most_points(result, expected)
