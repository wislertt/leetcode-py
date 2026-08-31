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
from helpers import assert_num_trees, run_num_trees
from solution import Solution

# %%
# Example test case
n = 3
expected = 5

# %%
result = run_num_trees(Solution, n)
result

# %%
assert_num_trees(result, expected)
