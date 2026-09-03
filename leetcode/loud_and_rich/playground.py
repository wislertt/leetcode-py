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
from helpers import assert_loud_and_rich, run_loud_and_rich
from solution import Solution

# %%
# Example test case
richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
quiet = [3, 2, 5, 4, 6, 1, 7, 0]
expected = [5, 5, 2, 5, 4, 5, 6, 7]

# %%
result = run_loud_and_rich(Solution, richer, quiet)
result

# %%
assert_loud_and_rich(result, expected)
