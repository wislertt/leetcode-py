# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_reorganize_string, run_reorganize_string
from solution import Solution

# %%
# Example test case
s = "aab"
expected = "aba"

# %%
result = run_reorganize_string(Solution, s)
result

# %%
assert_reorganize_string(result, s)
