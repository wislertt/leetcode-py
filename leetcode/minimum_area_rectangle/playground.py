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
from helpers import assert_min_area_rect, run_min_area_rect
from solution import Solution

# %%
# Example test case
points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
expected = 4

# %%
result = run_min_area_rect(Solution, points)
result

# %%
assert_min_area_rect(result, expected)
