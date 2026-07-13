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
from helpers import assert_gcd_of_strings, run_gcd_of_strings
from solution import Solution

# %%
# Example test case
str1 = "ABCABC"
str2 = "ABC"
expected = "ABC"

# %%
result = run_gcd_of_strings(Solution, str1, str2)
result

# %%
assert_gcd_of_strings(result, expected)
