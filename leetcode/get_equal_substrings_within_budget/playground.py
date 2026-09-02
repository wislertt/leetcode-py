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
from helpers import assert_equal_substring, run_equal_substring
from solution import Solution

# %%
# Example test case
s = "abcd"
t = "bcdf"
max_cost = 3
expected = 3

# %%
result = run_equal_substring(Solution, s, t, max_cost)
result

# %%
assert_equal_substring(result, expected)
