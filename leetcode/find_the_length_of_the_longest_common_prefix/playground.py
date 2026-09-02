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
from helpers import assert_longest_common_prefix, run_longest_common_prefix
from solution import Solution

# %%
# Example test case
arr1: list[int] = [1, 10, 100]
arr2: list[int] = [1000]
expected = 3

# %%
result = run_longest_common_prefix(Solution, arr1, arr2)
result

# %%
assert_longest_common_prefix(result, expected)
