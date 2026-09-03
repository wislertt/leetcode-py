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
from helpers import assert_three_sum_multiplicity, run_three_sum_multiplicity
from solution import Solution

# %%
# Example test case
arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
target = 8
expected = 20

# %%
result = run_three_sum_multiplicity(Solution, arr, target)
result

# %%
assert_three_sum_multiplicity(result, expected)
