# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_is_bipartite, run_is_bipartite
from solution import Solution

# %%
# Example test case
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
expected = True

# %%
result = run_is_bipartite(Solution, graph)
result

# %%
assert_is_bipartite(result, expected)
