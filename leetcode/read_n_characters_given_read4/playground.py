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
from helpers import assert_read, run_read
from solution import Solution

# %%
# Example test case
file = "abcde"
n = 5
expected = 5

# %%
result = run_read(Solution, file, n)
result

# %%
assert_read(result, expected)
