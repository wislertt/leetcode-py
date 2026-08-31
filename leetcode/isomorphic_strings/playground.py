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
from helpers import assert_is_isomorphic, run_is_isomorphic
from solution import Solution

# %%
# Example test case
s = "egg"
t = "add"
expected = True

# %%
result = run_is_isomorphic(Solution, s, t)
result

# %%
assert_is_isomorphic(result, expected)
