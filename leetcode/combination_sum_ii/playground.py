# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_combination_sum2, run_combination_sum2
from solution import Solution

# %%
# Example test case
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

# %%
result = run_combination_sum2(Solution, candidates, target)
result

# %%
assert_combination_sum2(result, expected)
