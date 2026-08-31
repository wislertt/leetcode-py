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
from helpers import assert_smallest_from_leaf, run_smallest_from_leaf
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [0, 1, 2, 3, 4, 3, 4]
expected = "dba"

# %%
result = run_smallest_from_leaf(Solution, root_list)
result

# %%
assert_smallest_from_leaf(result, expected)
