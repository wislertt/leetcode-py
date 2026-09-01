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
from helpers import assert_minimize_xor, run_minimize_xor
from solution import Solution

# %%
# Example test case
num1 = 3
num2 = 5
expected = 3

# %%
result = run_minimize_xor(Solution, num1, num2)
result

# %%
assert_minimize_xor(result, expected)
