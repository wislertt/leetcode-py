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
from helpers import assert_max_width_of_vertical_area, run_max_width_of_vertical_area
from solution import Solution

# %%
# Example test case
points: list[list[int]] = [[8, 7], [9, 9], [7, 4], [9, 7]]
expected: int = 1

# %%
result = run_max_width_of_vertical_area(Solution, points)
result

# %%
assert_max_width_of_vertical_area(result, expected)
