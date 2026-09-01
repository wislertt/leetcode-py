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
from helpers import assert_max_ascending_sum, run_max_ascending_sum
from solution import Solution

# %%
# Example test case
nums = [10, 20, 30, 5, 10, 50]
expected = 65

# %%
result = run_max_ascending_sum(Solution, nums)
result

# %%
assert_max_ascending_sum(result, expected)
