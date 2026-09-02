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
from helpers import assert_transform_array, run_transform_array
from solution import Solution

# %%
# Example test case
arr = [6, 2, 3, 4]
expected = [6, 3, 3, 4]

# %%
result = run_transform_array(Solution, arr)
result

# %%
assert_transform_array(result, expected)
