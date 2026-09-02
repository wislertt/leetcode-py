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
from helpers import assert_add_strings, run_add_strings
from solution import Solution

# %%
# Example test case
num1 = "11"
num2 = "123"
expected = "134"

# %%
result = run_add_strings(Solution, num1, num2)
result

# %%
assert_add_strings(result, expected)
