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
from helpers import assert_get_intersection_node, run_get_intersection_node
from solution import Solution

# %%
# Example test case
list_a: list[int] = [4, 1, 8, 4, 5]
list_b: list[int] = [5, 6, 1, 8, 4, 5]
skip_a: int = 2
skip_b: int = 3

# %%
result, expected = run_get_intersection_node(Solution, list_a, list_b, skip_a, skip_b)
result

# %%
assert_get_intersection_node(result, expected)
