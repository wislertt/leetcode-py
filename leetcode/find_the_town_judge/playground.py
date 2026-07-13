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
from helpers import assert_find_judge, run_find_judge
from solution import Solution

# %%
# Example test case
n = 3
trust = [[1, 3], [2, 3]]
expected = 3

# %%
result = run_find_judge(Solution, n, trust)
result

# %%
assert_find_judge(result, expected)
