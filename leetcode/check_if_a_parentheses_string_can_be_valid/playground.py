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
from helpers import assert_can_be_valid, run_can_be_valid
from solution import Solution

# %%
# Example test case
s = "))()))"
locked = "010100"
expected = True

# %%
result = run_can_be_valid(Solution, s, locked)
result

# %%
assert_can_be_valid(result, expected)
