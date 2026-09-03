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
from helpers import assert_large_group_positions, run_large_group_positions
from solution import Solution

# %%
# Example test case
s = "abbxxxxzzy"
expected = [[3, 6]]

# %%
result = run_large_group_positions(Solution, s)
result

# %%
assert_large_group_positions(result, expected)
