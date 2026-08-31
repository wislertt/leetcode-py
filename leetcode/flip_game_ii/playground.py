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
from helpers import assert_can_win, run_can_win
from solution import Solution

# %%
# Example test case
current_state = "++++"
expected = True

# %%
result = run_can_win(Solution, current_state)
result

# %%
assert_can_win(result, expected)
