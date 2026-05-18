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
from helpers import assert_clone_graph, run_clone_graph
from solution import Solution

# %%
# Example test case
adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]

# %%
result = run_clone_graph(Solution, adj_list)
result

# %%
assert_clone_graph(result, adj_list)
