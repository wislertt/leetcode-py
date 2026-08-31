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
from helpers import assert_count_orders, run_count_orders
from solution import Solution

# %%
# Example test case
n = 3
expected = 90

# %%
result = run_count_orders(Solution, n)
result

# %%
assert_count_orders(result, expected)
