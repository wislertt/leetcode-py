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
from helpers import assert_maximum_candies, run_maximum_candies
from solution import Solution

# %%
# Example test case
candies = [5, 8, 6]
k = 3
expected = 5

# %%
result = run_maximum_candies(Solution, candies, k)
result

# %%
assert_maximum_candies(result, expected)
