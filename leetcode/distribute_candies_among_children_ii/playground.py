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
from helpers import assert_distribute_candies, run_distribute_candies
from solution import Solution

# %%
# Example test case
n = 5
limit = 2
expected = 3

# %%
result = run_distribute_candies(Solution, n, limit)
result

# %%
assert_distribute_candies(result, expected)
