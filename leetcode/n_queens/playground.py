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
from helpers import assert_solve_n_queens, run_solve_n_queens
from solution import Solution

# %%
# Example test case
n = 4
expected = [["..Q.", "Q...", "...Q", ".Q.."], [".Q..", "...Q", "Q...", "..Q."]]

# %%
result = run_solve_n_queens(Solution, n)
result

# %%
assert_solve_n_queens(result, expected)
