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
from helpers import assert_third_max, run_third_max
from solution import Solution

# %%
# Example test case
nums = [3, 2, 1]
expected = 1

# %%
result = run_third_max(Solution, nums)
result

# %%
assert_third_max(result, expected)
