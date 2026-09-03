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
from helpers import assert_soup_servings, run_soup_servings
from solution import Solution

# %%
# Example test case
n = 50
expected = 0.625

# %%
result = run_soup_servings(Solution, n)
result

# %%
assert_soup_servings(result, expected)
