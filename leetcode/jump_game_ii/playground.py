# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_jump, run_jump
from solution import Solution

# %%
# Example test case
nums: list[int] = [2, 3, 1, 1, 4]
expected = 2

# %%
result = run_jump(Solution, nums)
result

# %%
assert_jump(result, expected)
