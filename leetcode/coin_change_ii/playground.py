# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_change, run_change
from solution import Solution

# %%
# Example test case
amount = 5
coins = [1, 2, 5]
expected = 4

# %%
result = run_change(Solution, amount, coins)
result

# %%
assert_change(result, expected)
