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
from helpers import assert_fraction_addition, run_fraction_addition
from solution import Solution

# %%
# Example test case
expression = "-1/2+1/2"
expected = "0/1"

# %%
result = run_fraction_addition(Solution, expression)
result

# %%
assert_fraction_addition(result, expected)
