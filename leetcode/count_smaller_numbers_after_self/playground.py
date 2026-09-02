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
from helpers import assert_count_smaller, run_count_smaller
from solution import Solution

# %%
# Example test case
nums = [5, 2, 6, 1]
expected = [2, 1, 1, 0]

# %%
result = run_count_smaller(Solution, nums)
result

# %%
assert_count_smaller(result, expected)
