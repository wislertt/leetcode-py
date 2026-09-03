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
from helpers import assert_racecar, run_racecar
from solution import Solution

# %%
# Example test case
target = 3
expected = 2

# %%
result = run_racecar(Solution, target)
result

# %%
assert_racecar(result, expected)
