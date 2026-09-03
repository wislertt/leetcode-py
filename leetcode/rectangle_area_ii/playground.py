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
from helpers import assert_rectangle_area, run_rectangle_area
from solution import Solution

# %%
# Example test case
rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
expected = 6

# %%
result = run_rectangle_area(Solution, rectangles)
result

# %%
assert_rectangle_area(result, expected)
