# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_min_window, run_min_window
from solution import Solution

# %%
# Example test case
s = "ADOBECODEBANC"
t = "ABC"
expected = "BANC"

# %%
result = run_min_window(Solution, s, t)
result

# %%
assert_min_window(result, expected)
