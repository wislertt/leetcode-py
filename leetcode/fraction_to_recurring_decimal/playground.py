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
from helpers import assert_fraction_to_decimal, run_fraction_to_decimal
from solution import Solution

# %%
# Example test case
numerator = 4
denominator = 333
expected = "0.(012)"

# %%
result = run_fraction_to_decimal(Solution, numerator, denominator)
result

# %%
assert_fraction_to_decimal(result, expected)
