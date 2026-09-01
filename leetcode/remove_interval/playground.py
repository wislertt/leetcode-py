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
from helpers import assert_remove_interval, run_remove_interval
from solution import Solution

# %%
# Example test case
intervals = [[0, 2], [3, 4], [5, 7]]
to_be_removed = [1, 6]
expected = [[0, 1], [6, 7]]

# %%
result = run_remove_interval(Solution, intervals, to_be_removed)
result

# %%
assert_remove_interval(result, expected)
