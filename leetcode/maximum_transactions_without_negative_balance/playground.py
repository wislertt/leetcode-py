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
from helpers import assert_max_transactions, run_max_transactions
from solution import Solution

# %%
# Example test case
transactions = [2, -5, 3, -1, -2]
expected = 4

# %%
result = run_max_transactions(Solution, transactions)
result

# %%
assert_max_transactions(result, expected)
