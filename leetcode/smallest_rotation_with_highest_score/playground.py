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
from helpers import assert_best_rotation, run_best_rotation
from solution import Solution

# %%
# Example test case
nums = [2, 3, 1, 4, 0]
expected = 3

# %%
result = run_best_rotation(Solution, nums)
result

# %%
assert_best_rotation(result, expected)
