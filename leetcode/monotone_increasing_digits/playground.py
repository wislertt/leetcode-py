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
from helpers import assert_monotone_increasing_digits, run_monotone_increasing_digits
from solution import Solution

# %%
# Example test case
n = 332
expected = 299

# %%
result = run_monotone_increasing_digits(Solution, n)
result

# %%
assert_monotone_increasing_digits(result, expected)
