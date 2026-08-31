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
from helpers import assert_find_min_arrow_shots, run_find_min_arrow_shots
from solution import Solution

# %%
# Example test case
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
expected = 2

# %%
result = run_find_min_arrow_shots(Solution, points)
result

# %%
assert_find_min_arrow_shots(result, expected)
