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
from helpers import assert_integer_replacement, run_integer_replacement
from solution import Solution

# %%
# Example test case
n = 8
expected = 3

# %%
result = run_integer_replacement(Solution, n)
result

# %%
assert_integer_replacement(result, expected)
