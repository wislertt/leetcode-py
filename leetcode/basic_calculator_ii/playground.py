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
from helpers import assert_calculate, run_calculate
from solution import Solution

# %%
# Example test case
s = "3+2*2"
expected = 7

# %%
result = run_calculate(Solution, s)
result

# %%
assert_calculate(result, expected)
