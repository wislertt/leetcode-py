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
from helpers import assert_profitable_schemes, run_profitable_schemes
from solution import Solution

# %%
# Example test case
n = 5
min_profit = 3
group = [2, 2]
profit = [2, 3]
expected = 2

# %%
result = run_profitable_schemes(Solution, n, min_profit, group, profit)
result

# %%
assert_profitable_schemes(result, expected)
