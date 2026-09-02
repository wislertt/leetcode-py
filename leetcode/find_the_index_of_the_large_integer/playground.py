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
from helpers import assert_get_index, run_get_index
from solution import Solution

# %%
# Example test case
arr = [7, 7, 7, 7, 10, 7, 7, 7]
expected = 4

# %%
result = run_get_index(Solution, arr)
result

# %%
assert_get_index(result, expected)
