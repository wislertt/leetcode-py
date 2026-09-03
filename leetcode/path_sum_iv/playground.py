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
from helpers import assert_path_sum, run_path_sum
from solution import Solution

# %%
# Example test case
nums: list[int] = [113, 215, 221]
expected = 12

# %%
result = run_path_sum(Solution, nums)
result

# %%
assert_path_sum(result, expected)
