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
from helpers import assert_guess_number, run_guess_number
from solution import Solution

# %%
# Example test case
n = 10
pick = 6
expected = 6

# %%
result = run_guess_number(Solution, n, pick)
result

# %%
assert_guess_number(result, expected)
