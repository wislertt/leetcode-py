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
from helpers import assert_leads_to_destination, run_leads_to_destination
from solution import Solution

# %%
# Example test case
n = 4
edges = [[0, 1], [0, 3], [1, 2], [2, 1]]
source = 0
destination = 3
expected = False

# %%
result = run_leads_to_destination(Solution, n, edges, source, destination)
result

# %%
assert_leads_to_destination(result, expected)
