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
from helpers import assert_verify_preorder, run_verify_preorder
from solution import Solution

# %%
# Example test case
preorder = [5, 2, 1, 3, 6]
expected = True

# %%
result = run_verify_preorder(Solution, preorder)
result

# %%
assert_verify_preorder(result, expected)
