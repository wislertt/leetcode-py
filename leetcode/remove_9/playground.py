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
from helpers import assert_new_integer, run_new_integer
from solution import Solution

# %%
# Example test case
n = 9
expected = 10

# %%
result = run_new_integer(Solution, n)
result

# %%
assert_new_integer(result, expected)
