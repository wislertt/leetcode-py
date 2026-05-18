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
from helpers import assert_can_construct, run_can_construct
from solution import Solution

# %%
# Example test case
ransom_note = "aa"
magazine = "aab"
expected = True

# %%
result = run_can_construct(Solution, ransom_note, magazine)
result

# %%
assert_can_construct(result, expected)
