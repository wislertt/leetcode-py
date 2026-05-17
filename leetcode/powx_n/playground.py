# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_my_pow, run_my_pow
from solution import Solution

# %%
# Example test case
x = 2.0
n = 10
expected = 1024.0

# %%
result = run_my_pow(Solution, x, n)
result

# %%
assert_my_pow(result, expected)
