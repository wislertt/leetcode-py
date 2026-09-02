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
from helpers import assert_divide_players, run_divide_players
from solution import Solution

# %%
# Example test case
skill = [3, 2, 5, 1, 3, 4]
expected = 22

# %%
result = run_divide_players(Solution, skill)
result

# %%
assert_divide_players(result, expected)
