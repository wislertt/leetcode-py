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
from helpers import assert_last_stone_weight, run_last_stone_weight
from solution import Solution

# %%
# Example test case
stones = [2, 7, 4, 1, 8, 1]
expected = 1

# %%
result = run_last_stone_weight(Solution, stones)
result

# %%
assert_last_stone_weight(result, expected)
