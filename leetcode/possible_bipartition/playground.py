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
from helpers import assert_possible_bipartition, run_possible_bipartition
from solution import Solution

# %%
# Example test case
n = 4
dislikes = [[1, 2], [1, 3], [2, 4]]
expected = True

# %%
result = run_possible_bipartition(Solution, n, dislikes)
result

# %%
assert_possible_bipartition(result, expected)
