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
from helpers import assert_summary_ranges, run_summary_ranges
from solution import Solution

# %%
# Example test case
nums = [0, 1, 2, 4, 5, 7]
expected = ["0->2", "4->5", "7"]

# %%
result = run_summary_ranges(Solution, nums)
result

# %%
assert_summary_ranges(result, expected)
