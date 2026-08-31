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
from helpers import assert_construct_from_pre_post, run_construct_from_pre_post
from solution import Solution

# %%
# Example test case
preorder = [1, 2, 4, 5, 3, 6, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]
expected = [[1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]]

# %%
result = run_construct_from_pre_post(Solution, preorder, postorder)
result

# %%
assert_construct_from_pre_post(result, expected)
