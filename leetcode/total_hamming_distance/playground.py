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
from helpers import assert_total_hamming_distance, run_total_hamming_distance
from solution import Solution

# %%
# Example test case
nums = [4, 14, 2]
expected = 6

# %%
result = run_total_hamming_distance(Solution, nums)
result

# %%
assert_total_hamming_distance(result, expected)
