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
from helpers import assert_evaluate_tree, run_evaluate_tree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [2, 1, 3, None, None, 0, 1]
expected = True

# %%
result = run_evaluate_tree(Solution, root_list)
result

# %%
assert_evaluate_tree(result, expected)
