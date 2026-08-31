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
from helpers import assert_two_city_sched_cost, run_two_city_sched_cost
from solution import Solution

# %%
# Example test case
costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
expected = 110

# %%
result = run_two_city_sched_cost(Solution, costs)
result

# %%
assert_two_city_sched_cost(result, expected)
