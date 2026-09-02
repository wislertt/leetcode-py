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
from helpers import assert_find_luslength, run_find_luslength
from solution import Solution

# %%
# Example test case
a = "aba"
b = "cdc"
expected = 3

# %%
result = run_find_luslength(Solution, a, b)
result

# %%
assert_find_luslength(result, expected)
