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
from helpers import assert_encode, run_encode
from solution import Solution

# %%
# Example test case
s = "aaaaaaaaaa"
expected_len = 5

# %%
result = run_encode(Solution, s)
result

# %%
assert_encode(result, s, expected_len)
