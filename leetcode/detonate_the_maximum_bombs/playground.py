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
from helpers import assert_maximum_detonation, run_maximum_detonation
from solution import Solution

# %%
# Example test case
bombs: list[list[int]] = [[2, 1, 3], [6, 1, 4]]
expected = 2

# %%
result = run_maximum_detonation(Solution, bombs)
result

# %%
assert_maximum_detonation(result, expected)
