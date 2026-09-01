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
from helpers import assert_count_complete_components, run_count_complete_components
from solution import Solution

# %%
# Example test case
n = 6
edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
expected = 3

# %%
result = run_count_complete_components(Solution, n, edges)
result

# %%
assert_count_complete_components(result, expected)
