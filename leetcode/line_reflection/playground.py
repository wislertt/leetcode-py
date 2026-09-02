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
from helpers import assert_is_reflected, run_is_reflected
from solution import Solution

# %%
# Example test case
points: list[list[int]] = [[1, 1], [-1, 1]]
expected = True

# %%
result = run_is_reflected(Solution, points)
result

# %%
assert_is_reflected(result, expected)
