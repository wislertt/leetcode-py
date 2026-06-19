# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_subsets_with_dup, run_subsets_with_dup
from solution import Solution

# %%
# Example test case
nums = [1, 2, 2]
expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

# %%
result = run_subsets_with_dup(Solution, nums)
result

# %%
assert_subsets_with_dup(result, expected)
