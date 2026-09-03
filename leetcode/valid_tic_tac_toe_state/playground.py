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
from helpers import assert_valid_tic_tac_toe, run_valid_tic_tac_toe
from solution import Solution

# %%
# Example test case
board = ["XOX", "O O", "XOX"]
expected = True

# %%
result = run_valid_tic_tac_toe(Solution, board)
result

# %%
assert_valid_tic_tac_toe(result, expected)
