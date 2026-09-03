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
from helpers import assert_min_area_free_rect, run_min_area_free_rect
from solution import Solution

# %%
# Example test case
points = [[1, 2], [2, 1], [1, 0], [0, 1]]
expected = 2.0

# %%
result = run_min_area_free_rect(Solution, points)
result

# %%
assert_min_area_free_rect(result, expected)
