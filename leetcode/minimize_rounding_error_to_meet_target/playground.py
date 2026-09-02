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
from helpers import assert_minimize_error, run_minimize_error
from solution import Solution

# %%
# Example test case
prices = ["0.700", "2.800", "4.900"]
target = 8
expected = "1.000"

# %%
result = run_minimize_error(Solution, prices, target)
result

# %%
assert_minimize_error(result, expected)
