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
from helpers import assert_minimize_max, run_minimize_max
from solution import Solution

# %%
# Example test case
nums = [10, 1, 2, 7, 1, 3]
p = 2
expected = 1

# %%
result = run_minimize_max(Solution, nums, p)
result

# %%
assert_minimize_max(result, expected)
