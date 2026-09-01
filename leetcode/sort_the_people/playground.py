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
from helpers import assert_sort_people, run_sort_people
from solution import Solution

# %%
# Example test case
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
expected = ["Mary", "Emma", "John"]

# %%
result = run_sort_people(Solution, names, heights)
result

# %%
assert_sort_people(result, expected)
