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
from helpers import assert_add_operators, run_add_operators
from solution import Solution

# %%
# Example test case
num = "123"
target = 6
expected = ["1*2*3", "1+2+3"]

# %%
result = run_add_operators(Solution, num, target)
result

# %%
assert_add_operators(result, expected)
