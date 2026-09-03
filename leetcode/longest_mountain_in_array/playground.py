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
from helpers import assert_longest_mountain, run_longest_mountain
from solution import Solution

# %%
# Example test case
arr: list[int] = [2, 1, 4, 7, 3, 2, 5]
expected: int = 5

# %%
result = run_longest_mountain(Solution, arr)
result

# %%
assert_longest_mountain(result, expected)
