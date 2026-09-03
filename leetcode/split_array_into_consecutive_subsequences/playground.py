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
from helpers import assert_is_possible, run_is_possible
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 3, 4, 5]
expected = True

# %%
result = run_is_possible(Solution, nums)
result

# %%
assert_is_possible(result, expected)
