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
from helpers import assert_is_scramble, run_is_scramble
from solution import Solution

# %%
# Example test case
s1 = "great"
s2 = "rgeat"
expected = True

# %%
result = run_is_scramble(Solution, s1, s2)
result

# %%
assert_is_scramble(result, expected)
