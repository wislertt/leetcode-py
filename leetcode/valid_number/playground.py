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
from helpers import assert_is_number, run_is_number
from solution import Solution

# %%
# Example test case
s = "0"
expected = True

# %%
result = run_is_number(Solution, s)
result

# %%
assert_is_number(result, expected)
