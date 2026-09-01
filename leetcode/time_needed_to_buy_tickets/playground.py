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
from helpers import assert_time_required_to_buy, run_time_required_to_buy
from solution import Solution

# %%
# Example test case
tickets = [2, 3, 2]
k = 2
expected = 6

# %%
result = run_time_required_to_buy(Solution, tickets, k)
result

# %%
assert_time_required_to_buy(result, expected)
