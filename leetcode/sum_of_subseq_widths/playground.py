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
from helpers import assert_sum_subseq_widths, run_sum_subseq_widths
from solution import Solution

# %%
# Example test case
nums = [2, 1, 3]
expected = 6

# %%
result = run_sum_subseq_widths(Solution, nums)
result

# %%
assert_sum_subseq_widths(result, expected)
