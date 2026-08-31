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
from helpers import assert_eventual_safe_nodes, run_eventual_safe_nodes
from solution import Solution

# %%
# Example test case
graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
expected = [2, 4, 5, 6]

# %%
result = run_eventual_safe_nodes(Solution, graph)
result

# %%
assert_eventual_safe_nodes(result, expected)
