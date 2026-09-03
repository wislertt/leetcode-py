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
from helpers import assert_sum_even_after_queries, run_sum_even_after_queries
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
expected = [8, 6, 2, 4]

# %%
result = run_sum_even_after_queries(Solution, nums, queries)
result

# %%
assert_sum_even_after_queries(result, expected)
