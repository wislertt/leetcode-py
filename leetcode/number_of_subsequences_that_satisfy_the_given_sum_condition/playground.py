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
from helpers import assert_num_subseq, run_num_subseq
from solution import Solution

# %%
# Example test case
nums = [3, 5, 6, 7]
target = 9
expected = 4

# %%
result = run_num_subseq(Solution, nums, target)
result

# %%
assert_num_subseq(result, expected)
