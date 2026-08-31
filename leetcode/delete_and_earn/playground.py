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
from helpers import assert_delete_and_earn, run_delete_and_earn
from solution import Solution

# %%
# Example test case
nums = [3, 4, 2]
expected = 6

# %%
result = run_delete_and_earn(Solution, nums)
result

# %%
assert_delete_and_earn(result, expected)
