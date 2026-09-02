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
from helpers import assert_combination_sum_3, run_combination_sum_3
from solution import Solution

# %%
# Example test case
k = 3
n = 7
expected = [[1, 2, 4]]

# %%
result = run_combination_sum_3(Solution, k, n)
result

# %%
assert_combination_sum_3(result, expected)
