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
from helpers import assert_can_win_nim, run_can_win_nim
from solution import Solution

# %%
# Example test case
n = 4
expected = False

# %%
result = run_can_win_nim(Solution, n)
result

# %%
assert_can_win_nim(result, expected)
