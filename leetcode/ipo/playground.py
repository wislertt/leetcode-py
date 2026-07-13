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
from helpers import assert_find_maximized_capital, run_find_maximized_capital
from solution import Solution

# %%
# Example test case
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
expected = 4

# %%
result = run_find_maximized_capital(Solution, k, w, profits, capital)
result

# %%
assert_find_maximized_capital(result, expected)
