# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_min_eating_speed, run_min_eating_speed
from solution import Solution

# %%
# Example test case
piles = [3, 6, 7, 11]
h = 8
expected = 4

# %%
result = run_min_eating_speed(Solution, piles, h)
result

# %%
assert_min_eating_speed(result, expected)
