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
from helpers import assert_min_cost, run_min_cost
from solution import Solution

# %%
# Example test case
costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
expected = 10

# %%
result = run_min_cost(Solution, costs)
result

# %%
assert_min_cost(result, expected)
