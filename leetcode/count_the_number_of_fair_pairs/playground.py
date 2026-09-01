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
from helpers import assert_count_fair_pairs, run_count_fair_pairs
from solution import Solution

# %%
# Example test case
nums: list[int] = [0, 1, 7, 4, 4, 5]
lower = 3
upper = 6
expected = 6

# %%
result = run_count_fair_pairs(Solution, nums, lower, upper)
result

# %%
assert_count_fair_pairs(result, expected)
