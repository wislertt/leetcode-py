# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_multiply, run_multiply
from solution import Solution

# %%
# Example test case
num1 = "123"
num2 = "456"
expected = "56088"

# %%
result = run_multiply(Solution, num1, num2)
result

# %%
assert_multiply(result, expected)
