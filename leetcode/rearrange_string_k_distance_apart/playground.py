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
from helpers import assert_rearrange_string, run_rearrange_string
from solution import Solution

# %%
# Example test case
s = "aabbcc"
k = 3

# %%
result = run_rearrange_string(Solution, s, k)
result

# %%
assert_rearrange_string(result, s, k)
