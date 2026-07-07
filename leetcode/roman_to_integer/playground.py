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
from helpers import assert_roman_to_int, run_roman_to_int
from solution import Solution

# %%
# Example test case
s = "MCMXCIV"
expected = 1994

# %%
result = run_roman_to_int(Solution, s)
result

# %%
assert_roman_to_int(result, expected)
