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
from helpers import assert_total_n_queens, run_total_n_queens
from solution import Solution

# %%
# Example test case
n = 4
expected = 2

# %%
result = run_total_n_queens(Solution, n)
result

# %%
assert_total_n_queens(result, expected)
