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
from helpers import assert_parse_bool_expr, run_parse_bool_expr
from solution import Solution

# %%
# Example test case
expression = "|(f, f, f, t)"
expected = True

# %%
result = run_parse_bool_expr(Solution, expression)
result

# %%
assert_parse_bool_expr(result, expected)
