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
from helpers import assert_get_final_state, run_get_final_state
from solution import Solution

# %%
# Example test case
nums = [2, 1, 3, 5, 6]
k = 5
multiplier = 2
expected = [8, 4, 6, 5, 6]

# %%
result = run_get_final_state(Solution, nums, k, multiplier)
result

# %%
assert_get_final_state(result, expected)
