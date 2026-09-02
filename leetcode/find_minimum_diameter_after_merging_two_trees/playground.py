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
from helpers import assert_minimum_diameter_after_merge, run_minimum_diameter_after_merge
from solution import Solution

# %%
# Example test case
edges1: list[list[int]] = [[0, 1], [0, 2], [0, 3]]
edges2: list[list[int]] = [[0, 1]]
expected = 3

# %%
result = run_minimum_diameter_after_merge(Solution, edges1, edges2)
result

# %%
assert_minimum_diameter_after_merge(result, expected)
