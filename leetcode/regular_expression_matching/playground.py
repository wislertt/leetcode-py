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
from helpers import assert_is_match, run_is_match
from solution import Solution

# %%
# Example test case
s = "aa"
p = "a*"
expected = True

# %%
result = run_is_match(Solution, s, p)
result

# %%
assert_is_match(result, expected)
