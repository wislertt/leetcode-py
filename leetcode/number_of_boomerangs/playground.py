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
from helpers import assert_number_of_boomerangs, run_number_of_boomerangs
from solution import Solution

# %%
# Example test case
points: list[list[int]] = [[0, 0], [1, 0], [2, 0]]
expected: int = 2

# %%
result = run_number_of_boomerangs(Solution, points)
print(f"Number of boomerangs: {result}")
result

# %%
assert_number_of_boomerangs(result, expected)
