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
from helpers import assert_successful_pairs, run_successful_pairs
from solution import Solution

# %%
# Example test case
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
expected = [4, 0, 3]

# %%
result = run_successful_pairs(Solution, spells, potions, success)
result

# %%
assert_successful_pairs(result, expected)
