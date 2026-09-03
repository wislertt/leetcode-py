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
from helpers import assert_triangle_number, run_triangle_number
from solution import Solution

# %%
# Example test case
nums = [2, 2, 3, 4]
expected = 3

# %%
result = run_triangle_number(Solution, nums)
result

# %%
assert_triangle_number(result, expected)
