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
from helpers import assert_optimal_division, run_optimal_division
from solution import Solution

# %%
# Example test case
nums = [1000, 100, 10, 2]
expected = "1000/(100/10/2)"

# %%
result = run_optimal_division(Solution, nums)
result

# %%
assert_optimal_division(result, expected)
