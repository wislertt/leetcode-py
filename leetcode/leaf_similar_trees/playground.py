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
from helpers import assert_leaf_similar, run_leaf_similar
from solution import Solution

# %%
# Example test case
root1_list: list[int | None] = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
root2_list: list[int | None] = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
expected = True

# %%
result = run_leaf_similar(Solution, root1_list, root2_list)
result

# %%
assert_leaf_similar(result, expected)
