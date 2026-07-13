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
from helpers import assert_num_buses_to_destination, run_num_buses_to_destination
from solution import Solution

# %%
# Example test case
routes = [[1, 2, 7], [3, 6, 7]]
source = 1
target = 6
expected = 2

# %%
result = run_num_buses_to_destination(Solution, routes, source, target)
result

# %%
assert_num_buses_to_destination(result, expected)
