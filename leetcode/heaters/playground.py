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
from helpers import assert_find_radius, run_find_radius
from solution import Solution

# %%
# Example test case
houses = [1, 2, 3]
heaters = [2]
expected = 1

# %%
result = run_find_radius(Solution, houses, heaters)
result

# %%
assert_find_radius(result, expected)
