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
from helpers import assert_repeated_string_match, run_repeated_string_match
from solution import Solution

# %%
# Example test case
a = "abcd"
b = "cdabcdab"
expected = 3

# %%
result = run_repeated_string_match(Solution, a, b)
result

# %%
assert_repeated_string_match(result, expected)
