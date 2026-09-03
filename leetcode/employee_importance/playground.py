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
from helpers import assert_get_importance, run_get_importance
from solution import Solution

# %%
# Example test case
employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
id = 1
expected = 11

# %%
result = run_get_importance(Solution, employees, id)
result

# %%
assert_get_importance(result, expected)
