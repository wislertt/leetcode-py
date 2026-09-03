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
from helpers import assert_powerful_integers, run_powerful_integers
from solution import Solution

# %%
# Example test case
x = 2
y = 3
bound = 10
expected = [2, 3, 4, 5, 7, 9, 10]

# %%
result = run_powerful_integers(Solution, x, y, bound)
result

# %%
assert_powerful_integers(result, expected)
