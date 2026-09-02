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
from helpers import assert_find_min_step, run_find_min_step
from solution import Solution

# %%
# Example test case
board = "WWRRBBWW"
hand = "WRBRW"
expected = 2

# %%
result = run_find_min_step(Solution, board, hand)
result

# %%
assert_find_min_step(result, expected)
