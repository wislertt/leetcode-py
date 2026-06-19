# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_copy_random_list, run_copy_random_list
from solution import Solution

# %%
# Example test case (each node is [val, random_index])
nodes = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
expected = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

# %%
result = run_copy_random_list(Solution, nodes)
result

# %%
assert_copy_random_list(result, expected)
