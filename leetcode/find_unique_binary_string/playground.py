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
from helpers import assert_find_unique_binary_string, run_find_unique_binary_string
from solution import Solution

# %%
# Example test case
nums = ["01", "10"]
expected = "11"

# %%
result = run_find_unique_binary_string(Solution, nums)
result

# %%
assert_find_unique_binary_string(result, expected)
