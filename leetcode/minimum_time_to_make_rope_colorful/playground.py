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
colors = "abaac"
needed_time = [1, 2, 3, 4, 5]
expected = 3

# %%
result = run_min_cost(Solution, colors, needed_time)
result

# %%
assert_min_cost(result, expected)
