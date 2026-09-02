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
from helpers import assert_count_bad_pairs, run_count_bad_pairs
from solution import Solution

# %%
# Example test case
nums: list[int] = [4, 1, 3, 3]
expected = 5

# %%
result = run_count_bad_pairs(Solution, nums)
result

# %%
assert_count_bad_pairs(result, expected)
