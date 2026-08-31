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
from helpers import assert_min_diff_in_bst, run_min_diff_in_bst
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [4, 2, 6, 1, 3]
expected = 1

# %%
result = run_min_diff_in_bst(Solution, root_list)
result

# %%
assert_min_diff_in_bst(result, expected)
