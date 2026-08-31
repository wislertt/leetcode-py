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
from helpers import assert_is_convex, run_is_convex
from solution import Solution

# %%
# Example test case
points = [[0, 0], [0, 5], [5, 5], [5, 0]]
expected = True

# %%
result = run_is_convex(Solution, points)
result

# %%
assert_is_convex(result, expected)
