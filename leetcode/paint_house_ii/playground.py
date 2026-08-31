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
from helpers import assert_min_cost_ii, run_min_cost_ii
from solution import Solution

# %%
# Example test case
costs = [[1, 5, 3], [2, 9, 4]]
expected = 5

# %%
result = run_min_cost_ii(Solution, costs)
result

# %%
assert_min_cost_ii(result, expected)
