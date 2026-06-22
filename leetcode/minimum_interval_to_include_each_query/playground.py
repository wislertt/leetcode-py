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
from helpers import assert_min_interval, run_min_interval
from solution import Solution

# %%
# Example test case
intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]
expected = [3, 3, 1, 4]

# %%
result = run_min_interval(Solution, intervals, queries)
result

# %%
assert_min_interval(result, expected)
