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
from helpers import assert_is_rational_equal, run_is_rational_equal
from solution import Solution

# %%
# Example test case
s = "0.(52)"
t = "0.5(25)"
expected = True

# %%
result = run_is_rational_equal(Solution, s, t)
result

# %%
assert_is_rational_equal(result, expected)
