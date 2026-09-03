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
from helpers import assert_num_factored_binary_trees, run_num_factored_binary_trees
from solution import Solution

# %%
# Example test case
arr = [2, 4]
expected = 3

# %%
result = run_num_factored_binary_trees(Solution, arr)
result

# %%
assert_num_factored_binary_trees(result, expected)
