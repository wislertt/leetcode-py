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
from helpers import assert_remove_covered_intervals, run_remove_covered_intervals
from solution import Solution

# %%
# Example test case
intervals = [[1, 4], [3, 6], [2, 8]]
expected = 2

# %%
result = run_remove_covered_intervals(Solution, intervals)
result

# %%
assert_remove_covered_intervals(result, expected)
