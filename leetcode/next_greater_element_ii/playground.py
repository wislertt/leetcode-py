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
from helpers import assert_next_greater_elements, run_next_greater_elements
from solution import Solution

# %%
# Example test case
nums = [1, 2, 1]
expected = [2, -1, 2]

# %%
result = run_next_greater_elements(Solution, nums)
result

# %%
assert_next_greater_elements(result, expected)
