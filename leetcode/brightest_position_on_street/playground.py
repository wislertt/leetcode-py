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
from helpers import assert_brightest_position, run_brightest_position
from solution import Solution

# %%
# Example test case
lights: list[list[int]] = [[-3, 2], [1, 2], [3, 3]]
expected: int = -1

# %%
result = run_brightest_position(Solution, lights)
result

# %%
assert_brightest_position(result, expected)
