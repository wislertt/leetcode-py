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
from helpers import assert_minmax_gas_dist, run_minmax_gas_dist
from solution import Solution

# %%
# Example test case
stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 9
expected = 0.5

# %%
result = run_minmax_gas_dist(Solution, stations, k)
result

# %%
assert_minmax_gas_dist(result, expected)
