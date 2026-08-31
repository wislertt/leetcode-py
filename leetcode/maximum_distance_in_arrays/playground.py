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
from helpers import assert_max_distance, run_max_distance
from solution import Solution

# %%
# Example test case
arrays: list[list[int]] = [[1, 2, 3], [4, 5], [1, 2, 3]]
expected = 4

# %%
result = run_max_distance(Solution, arrays)
result

# %%
assert_max_distance(result, expected)
