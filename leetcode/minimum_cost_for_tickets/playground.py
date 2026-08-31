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
from helpers import assert_min_cost_tickets, run_min_cost_tickets
from solution import Solution

# %%
# Example test case
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
expected = 11

# %%
result = run_min_cost_tickets(Solution, days, costs)
result

# %%
assert_min_cost_tickets(result, expected)
