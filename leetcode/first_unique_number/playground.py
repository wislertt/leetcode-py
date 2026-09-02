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
from helpers import assert_first_unique, run_first_unique
from solution import FirstUnique

# %%
# Example test case
operations = [
    "FirstUnique",
    "show_first_unique",
    "add",
    "show_first_unique",
    "add",
    "show_first_unique",
    "add",
    "show_first_unique",
]
inputs = [[2, 3, 5], [], [5], [], [2], [], [3], []]
expected = [None, 2, None, 2, None, 3, None, -1]

# %%
result, first_unique = run_first_unique(FirstUnique, operations, inputs)
print(result)
first_unique

# %%
assert_first_unique(result, expected)
