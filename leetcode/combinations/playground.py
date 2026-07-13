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
from helpers import assert_combine, run_combine
from solution import Solution

# %%
# Example test case
n = 4
k = 2
expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# %%
result = run_combine(Solution, n, k)
result

# %%
assert_combine(result, expected)
