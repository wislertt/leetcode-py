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
from helpers import assert_remove_invalid_parentheses, run_remove_invalid_parentheses
from solution import Solution

# %%
# Example test case
s = "()())()"
expected = ["(())()", "()()()"]

# %%
result = run_remove_invalid_parentheses(Solution, s)
result

# %%
assert_remove_invalid_parentheses(result, expected)
