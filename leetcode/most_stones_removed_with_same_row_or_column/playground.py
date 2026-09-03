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
from helpers import assert_remove_stones, run_remove_stones
from solution import Solution

# %%
# Example test case
stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
expected = 5

# %%
result = run_remove_stones(Solution, stones)
result

# %%
assert_remove_stones(result, expected)
