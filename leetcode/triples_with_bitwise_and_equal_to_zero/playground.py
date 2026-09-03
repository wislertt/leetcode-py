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
from helpers import assert_count_triplets, run_count_triplets
from solution import Solution

# %%
# Example test case
nums = [2, 1, 3]
expected = 12

# %%
result = run_count_triplets(Solution, nums)
result

# %%
assert_count_triplets(result, expected)
