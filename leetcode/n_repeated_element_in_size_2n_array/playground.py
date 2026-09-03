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
from helpers import assert_repeated_n_times, run_repeated_n_times
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 3]
expected = 3

# %%
result = run_repeated_n_times(Solution, nums)
result

# %%
assert_repeated_n_times(result, expected)
