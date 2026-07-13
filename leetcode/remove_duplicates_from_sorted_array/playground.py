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
from helpers import assert_remove_duplicates, run_remove_duplicates
from solution import Solution

# %%
# Example test case
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expected = (5, [0, 1, 2, 3, 4])

# %%
result = run_remove_duplicates(Solution, nums)
result

# %%
assert_remove_duplicates(result, expected)
