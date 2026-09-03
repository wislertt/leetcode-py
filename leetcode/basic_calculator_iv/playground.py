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
from helpers import assert_basic_calculator_iv, run_basic_calculator_iv
from solution import Solution

# %%
# Example test case
expression = "e + 8 - a + 5"
evalvars = ["e"]
evalints = [1]
expected = ["-1*a", "14"]

# %%
result = run_basic_calculator_iv(Solution, expression, evalvars, evalints)
result

# %%
assert_basic_calculator_iv(result, expected)
