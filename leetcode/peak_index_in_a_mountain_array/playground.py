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
from helpers import assert_peak_index_in_mountain_array, run_peak_index_in_mountain_array
from solution import Solution

# %%
# Example test case
arr = [0, 2, 1, 0]
expected = 1

# %%
result = run_peak_index_in_mountain_array(Solution, arr)
result

# %%
assert_peak_index_in_mountain_array(result, expected)
