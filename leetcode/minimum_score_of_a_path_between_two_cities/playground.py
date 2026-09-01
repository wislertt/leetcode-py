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
from helpers import assert_min_score, run_min_score
from solution import Solution

# %%
# Example test case
n = 4
roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
expected = 5

# %%
result = run_min_score(Solution, n, roads)
result

# %%
assert_min_score(result, expected)
