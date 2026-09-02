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
from helpers import assert_sort_jumbled, run_sort_jumbled
from solution import Solution

# %%
# Example test case
mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
nums = [991, 338, 38]
expected = [338, 38, 991]

# %%
result = run_sort_jumbled(Solution, mapping, nums)
result

# %%
assert_sort_jumbled(result, expected)
