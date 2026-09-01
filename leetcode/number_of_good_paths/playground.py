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
from helpers import assert_number_of_good_paths, run_number_of_good_paths
from solution import Solution

# %%
# Example test case
vals = [1, 3, 2, 1, 3]
edges = [[0, 1], [0, 2], [2, 3], [2, 4]]
expected = 6

# %%
result = run_number_of_good_paths(Solution, vals, edges)
result

# %%
assert_number_of_good_paths(result, expected)
