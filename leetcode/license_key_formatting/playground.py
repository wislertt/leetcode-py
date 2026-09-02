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
from helpers import assert_license_key_formatting, run_license_key_formatting
from solution import Solution

# %%
# Example test case
s = "5F3Z-2e-9-w"
k = 4
expected = "5F3Z-2E9W"

# %%
result = run_license_key_formatting(Solution, s, k)
result

# %%
assert_license_key_formatting(result, expected)
