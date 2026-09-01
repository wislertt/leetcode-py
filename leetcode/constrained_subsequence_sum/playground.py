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
from helpers import assert_constrained_subset_sum, run_constrained_subset_sum
from solution import Solution

# %%
# Example test case
nums = [10, 2, -10, 5, 20]
k = 2
expected = 37

# %%
result = run_constrained_subset_sum(Solution, nums, k)
result

# %%
assert_constrained_subset_sum(result, expected)
