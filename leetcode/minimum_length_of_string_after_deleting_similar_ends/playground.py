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
from helpers import assert_minimum_length, run_minimum_length
from solution import Solution

# %%
# Example test case
s = "cabaabac"
expected = 0

# %%
result = run_minimum_length(Solution, s)
result

# %%
assert_minimum_length(result, expected)
