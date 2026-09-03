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
from helpers import assert_dominant_index, run_dominant_index
from solution import Solution

# %%
# Example test case
nums = [3, 6, 1, 0]
expected = 1

# %%
result = run_dominant_index(Solution, nums)
result

# %%
assert_dominant_index(result, expected)
