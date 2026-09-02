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
from helpers import assert_nodes_between_critical_points, run_nodes_between_critical_points
from solution import Solution

# %%
# Example test case
head_list = [5, 3, 1, 2, 5, 1, 2]
expected = [1, 3]

# %%
result = run_nodes_between_critical_points(Solution, head_list)
result

# %%
assert_nodes_between_critical_points(result, expected)
