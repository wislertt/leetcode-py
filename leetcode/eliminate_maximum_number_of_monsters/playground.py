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
from helpers import assert_eliminate_maximum, run_eliminate_maximum
from solution import Solution

# %%
# Example test case
dist: list[int] = [1, 3, 4]
speed: list[int] = [1, 1, 1]
expected: int = 3

# %%
result = run_eliminate_maximum(Solution, dist, speed)
result

# %%
assert_eliminate_maximum(result, expected)
