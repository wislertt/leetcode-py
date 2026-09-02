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
from helpers import assert_circular_array_loop, run_circular_array_loop
from solution import Solution

# %%
# Example test case
nums = [2, -1, 1, 2, 2]
expected = True

# %%
result = run_circular_array_loop(Solution, nums)
result

# %%
assert_circular_array_loop(result, expected)
