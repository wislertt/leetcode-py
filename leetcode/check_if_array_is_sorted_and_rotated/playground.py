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
from helpers import assert_check, run_check
from solution import Solution

# %%
# Example test case
nums = [3, 4, 5, 1, 2]
expected = True

# %%
result = run_check(Solution, nums)
result

# %%
assert_check(result, expected)
