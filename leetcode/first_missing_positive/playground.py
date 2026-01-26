# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_first_missing_positive, run_first_missing_positive
from solution import Solution

# %%
# Example test case
nums: list[int] = [1, 2, 0]
expected = 3

# %%
result = run_first_missing_positive(Solution, nums)
result

# %%
assert_first_missing_positive(result, expected)
