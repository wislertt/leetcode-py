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
from helpers import assert_make_largest_special, run_make_largest_special
from solution import Solution

# %%
# Example test case
s = "11011000"
expected = "11100100"

# %%
result = run_make_largest_special(Solution, s)
result

# %%
assert_make_largest_special(result, expected)
