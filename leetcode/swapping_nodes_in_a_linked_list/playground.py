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
from helpers import assert_swap_nodes, run_swap_nodes
from solution import Solution

# %%
# Example test case
head_list: list[int] = [1, 2, 3, 4, 5]
k = 2
expected: list[int] = [1, 4, 3, 2, 5]

# %%
result = run_swap_nodes(Solution, head_list, k)
result

# %%
assert_swap_nodes(result, expected)
