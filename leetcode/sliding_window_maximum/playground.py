# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_max_sliding_window, run_max_sliding_window
from solution import Solution

# %%
# Example test case
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
expected = [3, 3, 5, 5, 6, 7]

# %%
result = run_max_sliding_window(Solution, nums, k)
result

# %%
assert_max_sliding_window(result, expected)
