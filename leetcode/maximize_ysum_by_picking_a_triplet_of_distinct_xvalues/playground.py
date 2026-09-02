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
from helpers import assert_max_sum_distinct_triplet, run_max_sum_distinct_triplet
from solution import Solution

# %%
# Example test case
x = [1, 2, 1, 3, 2]
y = [5, 3, 4, 6, 2]
expected = 14

# %%
result = run_max_sum_distinct_triplet(Solution, x, y)
result

# %%
assert_max_sum_distinct_triplet(result, expected)
