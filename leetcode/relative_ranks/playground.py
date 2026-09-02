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
from helpers import assert_find_relative_ranks, run_find_relative_ranks
from solution import Solution

# %%
# Example test case
score = [5, 4, 3, 2, 1]
expected = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

# %%
result = run_find_relative_ranks(Solution, score)
result

# %%
assert_find_relative_ranks(result, expected)
