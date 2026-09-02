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
from helpers import assert_maximum_beauty, run_maximum_beauty
from solution import Solution

# %%
# Example test case
items: list[list[int]] = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
queries: list[int] = [1, 2, 3, 4, 5, 6]
expected: list[int] = [2, 4, 5, 5, 6, 6]

# %%
result = run_maximum_beauty(Solution, items, queries)
result

# %%
assert_maximum_beauty(result, expected)
