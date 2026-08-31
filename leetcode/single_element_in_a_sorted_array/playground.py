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
from helpers import assert_single_non_duplicate, run_single_non_duplicate
from solution import Solution

# %%
# Example test case
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
expected = 2

# %%
result = run_single_non_duplicate(Solution, nums)
result

# %%
assert_single_non_duplicate(result, expected)
