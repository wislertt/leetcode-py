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
from helpers import assert_is_array_special, run_is_array_special
from solution import Solution

# %%
# Example test case
nums = [2, 1, 4]
expected = True

# %%
result = run_is_array_special(Solution, nums)
result

# %%
assert_is_array_special(result, expected)
