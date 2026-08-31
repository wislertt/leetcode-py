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
from helpers import assert_strobogrammatic_in_range, run_strobogrammatic_in_range
from solution import Solution

# %%
# Example test case
low = "50"
high = "100"
expected = 3

# %%
result = run_strobogrammatic_in_range(Solution, low, high)
result

# %%
assert_strobogrammatic_in_range(result, expected)
