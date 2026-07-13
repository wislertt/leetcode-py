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
from helpers import assert_can_traverse_all_pairs, run_can_traverse_all_pairs
from solution import Solution

# %%
# Example test case
nums = [2, 3, 6]
expected = True

# %%
result = run_can_traverse_all_pairs(Solution, nums)
result

# %%
assert_can_traverse_all_pairs(result, expected)
