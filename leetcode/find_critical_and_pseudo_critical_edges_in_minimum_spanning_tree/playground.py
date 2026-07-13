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
from helpers import (
    assert_find_critical_and_pseudo_critical_edges,
    run_find_critical_and_pseudo_critical_edges,
)
from solution import Solution

# %%
# Example test case
n = 5
edges = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
expected = [[0, 1], [2, 3, 4, 5]]

# %%
result = run_find_critical_and_pseudo_critical_edges(Solution, n, edges)
result

# %%
assert_find_critical_and_pseudo_critical_edges(result, expected)
