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
from helpers import assert_is_one_edit_distance, run_is_one_edit_distance
from solution import Solution

# %%
# Example test case
s = "ab"
t = "acb"
expected = True

# %%
result = run_is_one_edit_distance(Solution, s, t)
result

# %%
assert_is_one_edit_distance(result, expected)
