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
from helpers import assert_can_i_win, run_can_i_win
from solution import Solution

# %%
# Example test case
max_choosable_integer = 10
desired_total = 11
expected = False

# %%
result = run_can_i_win(Solution, max_choosable_integer, desired_total)
result

# %%
assert_can_i_win(result, expected)
