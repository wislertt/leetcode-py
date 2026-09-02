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
from helpers import assert_original_digits, run_original_digits
from solution import Solution

# %%
# Example test case
s = "owoztneoer"
expected = "012"

# %%
result = run_original_digits(Solution, s)
result

# %%
assert_original_digits(result, expected)
