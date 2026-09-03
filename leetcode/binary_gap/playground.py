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
from helpers import assert_binary_gap, run_binary_gap
from solution import Solution

# %%
# Example test case
n = 22
expected = 2

# %%
result = run_binary_gap(Solution, n)
result

# %%
assert_binary_gap(result, expected)
