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
from helpers import assert_complex_number_multiply, run_complex_number_multiply
from solution import Solution

# %%
# Example test case
num1 = "1+1i"
num2 = "1+1i"
expected = "0+2i"

# %%
result = run_complex_number_multiply(Solution, num1, num2)
result

# %%
assert_complex_number_multiply(result, expected)
