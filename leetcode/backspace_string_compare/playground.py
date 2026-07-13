# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_backspace_compare, run_backspace_compare
from solution import Solution

# %%
# Example test case
s = "ab#c"
t = "ad#c"
expected = True

# %%
result = run_backspace_compare(Solution, s, t)
result

# %%
assert_backspace_compare(result, expected)
