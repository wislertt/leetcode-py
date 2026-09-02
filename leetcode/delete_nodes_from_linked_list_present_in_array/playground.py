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
from helpers import assert_modified_list, run_modified_list
from solution import Solution

# %%
# Example test case
nums: list[int] = [1, 2, 3]
head_vals: list[int] = [1, 2, 3, 4, 5]
expected_vals: list[int] = [4, 5]

# %%
result = run_modified_list(Solution, nums, head_vals)
result

# %%
assert_modified_list(result, expected_vals)
