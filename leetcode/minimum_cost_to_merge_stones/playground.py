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
from helpers import assert_merge_stones, run_merge_stones
from solution import Solution

# %%
# Example test case
stones = [3, 2, 4, 1]
k = 2
expected = 20

# %%
result = run_merge_stones(Solution, stones, k)
result

# %%
assert_merge_stones(result, expected)
