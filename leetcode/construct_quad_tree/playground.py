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
from helpers import assert_construct, run_construct
from solution import Solution

# %%
# Example test case (each node serialized as [isLeaf, val])
grid = [[0, 1], [1, 0]]
expected = [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]

# %%
result = run_construct(Solution, grid)
result

# %%
assert_construct(result, expected)
