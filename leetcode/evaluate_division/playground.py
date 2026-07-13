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
from helpers import assert_calc_equation, run_calc_equation
from solution import Solution

# %%
# Example test case
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
expected = [6.0, 0.5, -1.0, 1.0, -1.0]

# %%
result = run_calc_equation(Solution, equations, values, queries)
result

# %%
assert_calc_equation(result, expected)
