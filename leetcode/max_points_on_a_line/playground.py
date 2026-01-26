# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_max_points, run_max_points
from solution import Solution

# %%
# Example test case
points: list[list[int]] = [[1, 1], [2, 2], [3, 3]]
expected: int = 3

# %%
result = run_max_points(Solution, points)
print(f"Max points on a line: {result}")
result

# %%
assert_max_points(result, expected)
