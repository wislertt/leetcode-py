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
from helpers import assert_parse_ternary, run_parse_ternary
from solution import Solution

# %%
# Example test case
expression = "T?2:3"
expected = "2"

# %%
result = run_parse_ternary(Solution, expression)
result

# %%
assert_parse_ternary(result, expected)
