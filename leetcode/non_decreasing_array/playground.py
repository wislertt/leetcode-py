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
from helpers import assert_check_possibility, run_check_possibility
from solution import Solution

# %%
# Example test case
nums = [4, 2, 3]
expected = True

# %%
result = run_check_possibility(Solution, nums)
result

# %%
assert_check_possibility(result, expected)
