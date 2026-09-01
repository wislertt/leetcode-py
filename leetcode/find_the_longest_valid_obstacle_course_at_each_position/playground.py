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
from helpers import assert_longest_obstacle_course, run_longest_obstacle_course
from solution import Solution

# %%
# Example test case
obstacles: list[int] = [1, 2, 3, 2]
expected: list[int] = [1, 2, 3, 3]

# %%
result = run_longest_obstacle_course(Solution, obstacles)
result

# %%
assert_longest_obstacle_course(result, expected)
