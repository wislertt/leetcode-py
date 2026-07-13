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
from helpers import assert_tribonacci, run_tribonacci
from solution import Solution

# %%
# Example test case
n = 4
expected = 4

# %%
result = run_tribonacci(Solution, n)
result

# %%
assert_tribonacci(result, expected)
