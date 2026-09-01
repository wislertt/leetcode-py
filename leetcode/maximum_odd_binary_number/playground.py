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
from helpers import assert_maximum_odd_binary_number, run_maximum_odd_binary_number
from solution import Solution

# %%
# Example test case
s = "0101"
expected = "1001"

# %%
result = run_maximum_odd_binary_number(Solution, s)
result

# %%
assert_maximum_odd_binary_number(result, expected)
