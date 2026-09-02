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
from helpers import assert_num_rolls_to_target, run_num_rolls_to_target
from solution import Solution

# %%
# Example test case
n = 2
k = 6
target = 7
expected = 6

# %%
result = run_num_rolls_to_target(Solution, n, k, target)
result

# %%
assert_num_rolls_to_target(result, expected)
