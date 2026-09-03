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
from helpers import assert_num_special_equivalent_groups, run_num_special_equivalent_groups
from solution import Solution

# %%
# Example test case
words = ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]
expected = 3

# %%
result = run_num_special_equivalent_groups(Solution, words)
result

# %%
assert_num_special_equivalent_groups(result, expected)
