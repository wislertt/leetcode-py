# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_find_cheapest_price, run_find_cheapest_price
from solution import Solution

# %%
# Example test case
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
expected = 700

# %%
result = run_find_cheapest_price(Solution, n, flights, src, dst, k)
result

# %%
assert_find_cheapest_price(result, expected)
