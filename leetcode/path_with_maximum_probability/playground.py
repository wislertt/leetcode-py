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
from helpers import assert_max_probability, run_max_probability
from solution import Solution

# %%
# Example test case
n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succ_prob = [0.5, 0.5, 0.2]
start_node = 0
end_node = 2
expected = 0.25

# %%
result = run_max_probability(Solution, n, edges, succ_prob, start_node, end_node)
result

# %%
assert_max_probability(result, expected)
