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
from helpers import assert_subtree_with_all_deepest, run_subtree_with_all_deepest
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
expected_list: list[int | None] = [2, 7, 4]

# %%
result = run_subtree_with_all_deepest(Solution, root_list)
result

# %%
assert_subtree_with_all_deepest(result, expected_list)
