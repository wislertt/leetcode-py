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
from helpers import assert_can_place_flowers, run_can_place_flowers
from solution import Solution

# %%
# Example test case
flowerbed: list[int] = [1, 0, 0, 0, 1]
n = 1
expected = True

# %%
result = run_can_place_flowers(Solution, flowerbed, n)
result

# %%
assert_can_place_flowers(result, expected)
