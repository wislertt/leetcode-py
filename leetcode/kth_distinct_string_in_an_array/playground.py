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
from helpers import assert_kth_distinct, run_kth_distinct
from solution import Solution

# %%
# Example test case
arr = ["d", "b", "c", "b", "c", "a"]
k = 2
expected = "a"

# %%
result = run_kth_distinct(Solution, arr, k)
result

# %%
assert_kth_distinct(result, expected)
