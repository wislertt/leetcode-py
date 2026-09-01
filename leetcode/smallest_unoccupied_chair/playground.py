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
from helpers import assert_smallest_chair, run_smallest_chair
from solution import Solution

# %%
# Example test case
times = [[1, 4], [2, 3], [4, 6]]
target_friend = 1
expected = 1

# %%
result = run_smallest_chair(Solution, times, target_friend)
result

# %%
assert_smallest_chair(result, expected)
