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
from helpers import assert_are_almost_equal, run_are_almost_equal
from solution import Solution

# %%
# Example test case
s1 = "bank"
s2 = "kanb"
expected = True

# %%
result = run_are_almost_equal(Solution, s1, s2)
result

# %%
assert_are_almost_equal(result, expected)
