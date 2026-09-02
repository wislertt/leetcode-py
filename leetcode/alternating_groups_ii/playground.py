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
from helpers import assert_number_of_alternating_groups, run_number_of_alternating_groups
from solution import Solution

# %%
# Example test case
colors = [0, 1, 0, 1, 0]
k = 3
expected = 3

# %%
result = run_number_of_alternating_groups(Solution, colors, k)
result

# %%
assert_number_of_alternating_groups(result, expected)
