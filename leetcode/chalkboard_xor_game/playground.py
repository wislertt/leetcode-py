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
from helpers import assert_xor_game, run_xor_game
from solution import Solution

# %%
# Example test case
nums = [1, 1, 2]
expected = False

# %%
result = run_xor_game(Solution, nums)
result

# %%
assert_xor_game(result, expected)
