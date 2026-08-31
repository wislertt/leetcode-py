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
from helpers import assert_minimum_total, run_minimum_total
from solution import Solution

# %%
# Example test case
triangle: list[list[int]] = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
expected: int = 11

# %%
result = run_minimum_total(Solution, triangle)
result

# %%
assert_minimum_total(result, expected)
