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
from helpers import assert_max_difference, run_max_difference
from solution import Solution

# %%
# Example test case
s = "aaaaabbc"
expected = 3

# %%
result = run_max_difference(Solution, s)
result

# %%
assert_max_difference(result, expected)
