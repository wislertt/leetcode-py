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
from helpers import assert_num_components, run_num_components
from solution import Solution

# %%
# Example test case
head_vals: list[int] = [0, 1, 2, 3]
nums: list[int] = [0, 1, 3]
expected = 2

# %%
result = run_num_components(Solution, head_vals, nums)
result

# %%
assert_num_components(result, expected)
