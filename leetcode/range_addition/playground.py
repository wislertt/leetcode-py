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
from helpers import assert_get_modified_array, run_get_modified_array
from solution import Solution

# %%
# Example test case
length = 5
updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
expected = [-2, 0, 3, 5, 3]

# %%
result = run_get_modified_array(Solution, length, updates)
result

# %%
assert_get_modified_array(result, expected)
