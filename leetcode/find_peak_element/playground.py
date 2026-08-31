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
from helpers import assert_find_peak_element, run_find_peak_element
from solution import Solution

# %%
# Example test case
nums: list[int] = [1, 2, 3, 1]
expected: int = 2

# %%
result = run_find_peak_element(Solution, nums)
result

# %%
assert_find_peak_element(result, expected)
