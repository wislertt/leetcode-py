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
from helpers import assert_find_132pattern, run_find_132pattern
from solution import Solution

# %%
# Example test case
nums = [3, 1, 4, 2]
expected = True

# %%
result = run_find_132pattern(Solution, nums)
result

# %%
assert_find_132pattern(result, expected)
