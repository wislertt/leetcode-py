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
from helpers import assert_maximum_gain, run_maximum_gain
from solution import Solution

# %%
# Example test case
s = "cdbcbbaaabab"
x = 4
y = 5
expected = 19

# %%
result = run_maximum_gain(Solution, s, x, y)
result

# %%
assert_maximum_gain(result, expected)
