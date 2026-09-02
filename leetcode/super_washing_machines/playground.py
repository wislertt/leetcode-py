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
from helpers import assert_find_min_moves, run_find_min_moves
from solution import Solution

# %%
# Example test case
machines: list[int] = [1, 0, 5]
expected = 3

# %%
result = run_find_min_moves(Solution, machines)
result

# %%
assert_find_min_moves(result, expected)
