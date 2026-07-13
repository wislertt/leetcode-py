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
from helpers import assert_minimum_effort_path, run_minimum_effort_path
from solution import Solution

# %%
# Example test case
heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
expected = 2

# %%
result = run_minimum_effort_path(Solution, heights)
result

# %%
assert_minimum_effort_path(result, expected)
