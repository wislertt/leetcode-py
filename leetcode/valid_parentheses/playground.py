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
from helpers import assert_is_valid, run_is_valid
from solution import Solution

# %%
# Example test case
s = "()"
expected = True

# %%
result = run_is_valid(Solution, s)
result

# %%
assert_is_valid(result, expected)
