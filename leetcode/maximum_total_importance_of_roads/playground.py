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
from helpers import assert_maximum_importance, run_maximum_importance
from solution import Solution

# %%
# Example test case
n = 5
roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
expected = 43

# %%
result = run_maximum_importance(Solution, n, roads)
result

# %%
assert_maximum_importance(result, expected)
