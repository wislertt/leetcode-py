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
from helpers import assert_count_max_or_subsets, run_count_max_or_subsets
from solution import Solution

# %%
# Example test case
nums = [3, 1]
expected = 2

# %%
result = run_count_max_or_subsets(Solution, nums)
result

# %%
assert_count_max_or_subsets(result, expected)
