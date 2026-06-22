# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_merge_triplets, run_merge_triplets
from solution import Solution

# %%
# Example test case
triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target = [2, 7, 5]
expected = True

# %%
result = run_merge_triplets(Solution, triplets, target)
result

# %%
assert_merge_triplets(result, expected)
