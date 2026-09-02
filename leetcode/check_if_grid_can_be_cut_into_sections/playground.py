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
from helpers import assert_check_valid_cuts, run_check_valid_cuts
from solution import Solution

# %%
# Example test case
n = 5
rectangles = [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
expected = True

# %%
result = run_check_valid_cuts(Solution, n, rectangles)
result

# %%
assert_check_valid_cuts(result, expected)
