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
from helpers import assert_equations_possible, run_equations_possible
from solution import Solution

# %%
# Example test case
equations = ["a==b", "b!=a"]
expected = False

# %%
result = run_equations_possible(Solution, equations)
result

# %%
assert_equations_possible(result, expected)
