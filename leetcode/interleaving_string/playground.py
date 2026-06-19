# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_is_interleave, run_is_interleave
from solution import Solution

# %%
# Example test case
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
expected = True

# %%
result = run_is_interleave(Solution, s1, s2, s3)
result

# %%
assert_is_interleave(result, expected)
