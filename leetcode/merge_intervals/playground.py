# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_merge, run_merge
from solution import Solution

# %%
# Example test case
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
expected = [[1, 6], [8, 10], [15, 18]]

# %%
result = run_merge(Solution, intervals)
result

# %%
assert_merge(result, expected)
