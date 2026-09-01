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
from helpers import assert_can_be_equal, run_can_be_equal
from solution import Solution

# %%
# Example test case
target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]
expected = True

# %%
result = run_can_be_equal(Solution, target, arr)
result

# %%
assert_can_be_equal(result, expected)
