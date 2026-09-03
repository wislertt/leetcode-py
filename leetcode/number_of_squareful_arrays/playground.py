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
from helpers import assert_num_squareful_perms, run_num_squareful_perms
from solution import Solution

# %%
# Example test case
nums = [1, 17, 8]
expected = 2

# %%
result = run_num_squareful_perms(Solution, nums)
result

# %%
assert_num_squareful_perms(result, expected)
