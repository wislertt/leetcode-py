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
from helpers import assert_remove_duplicates, run_remove_duplicates
from solution import Solution

# %%
# Example test case
nums = [1, 1, 1, 2, 2, 3]
expected = (5, [1, 1, 2, 2, 3])

# %%
result = run_remove_duplicates(Solution, nums)
result

# %%
assert_remove_duplicates(result, expected)
