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
from helpers import assert_median_sliding_window, run_median_sliding_window
from solution import Solution

# %%
# Example test case
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]

# %%
result = run_median_sliding_window(Solution, nums, k)
result

# %%
assert_median_sliding_window(result, expected)
