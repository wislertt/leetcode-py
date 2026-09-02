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
from helpers import assert_calculate, run_calculate
from solution import Solution

# %%
# Example test case
s = "2*(5+5*2)/3+(6/2+8)"
expected = 21

# %%
result = run_calculate(Solution, s)
result

# %%
assert_calculate(result, expected)
