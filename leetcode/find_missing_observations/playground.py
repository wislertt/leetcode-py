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
from helpers import assert_missing_rolls, run_missing_rolls
from solution import Solution

# %%
# Example test case
rolls = [3, 2, 4, 3]
mean = 4
n = 2
expected = [6, 6]

# %%
result = run_missing_rolls(Solution, rolls, mean, n)
result

# %%
assert_missing_rolls(result, expected)
