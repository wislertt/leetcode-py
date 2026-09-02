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
from helpers import assert_has_all_codes, run_has_all_codes
from solution import Solution

# %%
# Example test case
s = "00110110"
k = 2
expected = True

# %%
result = run_has_all_codes(Solution, s, k)
result

# %%
assert_has_all_codes(result, expected)
