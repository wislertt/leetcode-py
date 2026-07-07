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
from helpers import assert_longest_valid_parentheses, run_longest_valid_parentheses
from solution import Solution

# %%
# Example test case
s = ")()())"
expected = 4

# %%
result = run_longest_valid_parentheses(Solution, s)
result

# %%
assert_longest_valid_parentheses(result, expected)
