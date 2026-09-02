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
from helpers import assert_closest_meeting_node, run_closest_meeting_node
from solution import Solution

# %%
# Example test case
edges = [2, 2, 3, -1]
node1 = 0
node2 = 1
expected = 2

# %%
result = run_closest_meeting_node(Solution, edges, node1, node2)
result

# %%
assert_closest_meeting_node(result, expected)
