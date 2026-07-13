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
from helpers import assert_get_order, run_get_order
from solution import Solution

# %%
# Example test case
tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
expected = [0, 2, 3, 1]

# %%
result = run_get_order(Solution, tasks)
result

# %%
assert_get_order(result, expected)
