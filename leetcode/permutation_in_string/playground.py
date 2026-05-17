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
from helpers import assert_check_inclusion, run_check_inclusion
from solution import Solution

# %%
# Example test case
s1 = "ab"
s2 = "eidbaooo"
expected = True

# %%
result = run_check_inclusion(Solution, s1, s2)
result

# %%
assert_check_inclusion(result, expected)
