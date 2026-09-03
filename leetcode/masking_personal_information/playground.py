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
from helpers import assert_mask_pii, run_mask_pii
from solution import Solution

# %%
# Example test case
s = "LeetCode@LeetCode.com"
expected = "l*****e@leetcode.com"

# %%
result = run_mask_pii(Solution, s)
result

# %%
assert_mask_pii(result, expected)
