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
from helpers import assert_num_squares, run_num_squares
from solution import Solution

# %%
# Example test case
n = 12
expected = 3

# %%
result = run_num_squares(Solution, n)
result

# %%
assert_num_squares(result, expected)
