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
from helpers import assert_nearest_palindromic, run_nearest_palindromic
from solution import Solution

# %%
# Example test case
n = "123"
expected = "121"

# %%
result = run_nearest_palindromic(Solution, n)
result

# %%
assert_nearest_palindromic(result, expected)
