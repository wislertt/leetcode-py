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
from helpers import assert_trailing_zeroes, run_trailing_zeroes
from solution import Solution

# %%
# Example test case
n = 5
expected = 1

# %%
result = run_trailing_zeroes(Solution, n)
result

# %%
assert_trailing_zeroes(result, expected)
