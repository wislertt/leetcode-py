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
from helpers import assert_is_rectangle_cover, run_is_rectangle_cover
from solution import Solution

# %%
# Example test case
rectangles: list[list[int]] = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
expected = True

# %%
result = run_is_rectangle_cover(Solution, rectangles)
result

# %%
assert_is_rectangle_cover(result, expected)
