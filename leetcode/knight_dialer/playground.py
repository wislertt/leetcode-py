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
from helpers import assert_knight_dialer, run_knight_dialer
from solution import Solution

# %%
# Example test case
n = 2
expected = 20

# %%
result = run_knight_dialer(Solution, n)
result

# %%
assert_knight_dialer(result, expected)
