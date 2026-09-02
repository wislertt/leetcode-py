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
from helpers import assert_linked_list_random_node, run_linked_list_random_node
from solution import Solution

# %%
# Example test case
operations = ["Solution", "get_random", "get_random", "get_random"]
inputs = [[1, 2, 3], [], [], []]
expected = [1, 2, 3]

# %%
result = run_linked_list_random_node(Solution, operations, inputs)
print(result)
result

# %%
assert_linked_list_random_node(result, expected)
