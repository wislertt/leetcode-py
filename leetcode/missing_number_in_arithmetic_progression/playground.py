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
from helpers import assert_missing_number, run_missing_number
from solution import Solution

# %%
# Example test case
arr = [5, 7, 11, 13]
expected = 9

# %%
result = run_missing_number(Solution, arr)
result

# %%
assert_missing_number(result, expected)
