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
from helpers import assert_evaluate, run_evaluate
from solution import Solution

# %%
# Example test case
expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
expected = 14

# %%
result = run_evaluate(Solution, expression)
result

# %%
assert_evaluate(result, expected)
