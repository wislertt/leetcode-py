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
from helpers import assert_min_groups, run_min_groups
from solution import Solution

# %%
# Example test case
intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
expected = 3

# %%
result = run_min_groups(Solution, intervals)
result

# %%
assert_min_groups(result, expected)
