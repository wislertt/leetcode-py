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
from helpers import assert_max_k_divisible_components, run_max_k_divisible_components
from solution import Solution

# %%
# Example test case
n = 5
edges = [[0, 2], [1, 2], [1, 3], [2, 4]]
values = [1, 8, 1, 4, 4]
k = 6
expected = 2

# %%
result = run_max_k_divisible_components(Solution, n, edges, values, k)
result

# %%
assert_max_k_divisible_components(result, expected)
