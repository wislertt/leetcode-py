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
from helpers import assert_solve_equation, run_solve_equation
from solution import Solution

# %%
# Example test case
equation = "x+5-3+x=6+x-2"
expected = "x=2"

# %%
result = run_solve_equation(Solution, equation)
result

# %%
assert_solve_equation(result, expected)
