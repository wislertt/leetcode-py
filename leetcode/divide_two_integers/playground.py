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
from helpers import assert_divide, run_divide
from solution import Solution

# %%
# Example test case
dividend = 10
divisor = 3
expected = 3

# %%
result = run_divide(Solution, dividend, divisor)
result

# %%
assert_divide(result, expected)
