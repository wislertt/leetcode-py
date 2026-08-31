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
from helpers import assert_generate_trees, run_generate_trees
from solution import Solution

# %%
# Example test case
n = 3
expected_tree: list[int | None] = [2, 1, 3]

# %%
result = run_generate_trees(Solution, n)
result

# %%
assert_generate_trees(result, n, expected_tree)
