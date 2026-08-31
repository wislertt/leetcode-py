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
from helpers import assert_min_transfers, run_min_transfers
from solution import Solution

# %%
# Example test case
transactions = [[0, 1, 10], [2, 0, 5]]
expected = 2

# %%
result = run_min_transfers(Solution, transactions)
result

# %%
assert_min_transfers(result, expected)
