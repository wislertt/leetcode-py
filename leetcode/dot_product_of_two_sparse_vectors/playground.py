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
from helpers import assert_dot_product, run_dot_product
from solution import SparseVector

# %%
# Example test case
nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]
expected = 8

# %%
result = run_dot_product(SparseVector, nums1, nums2)
result

# %%
assert_dot_product(result, expected)
