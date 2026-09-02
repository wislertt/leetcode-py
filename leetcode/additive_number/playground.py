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
from helpers import assert_is_additive_number, run_is_additive_number
from solution import Solution

# %%
# Example test case
num = "112358"
expected = True

# %%
result = run_is_additive_number(Solution, num)
result

# %%
assert_is_additive_number(result, expected)
