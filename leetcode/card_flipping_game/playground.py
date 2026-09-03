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
from helpers import assert_flipgame, run_flipgame
from solution import Solution

# %%
# Example test case
fronts: list[int] = [1, 2, 4, 4, 7]
backs: list[int] = [1, 3, 4, 1, 3]
expected = 2

# %%
result = run_flipgame(Solution, fronts, backs)
result

# %%
assert_flipgame(result, expected)
