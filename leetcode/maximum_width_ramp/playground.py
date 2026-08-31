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
from helpers import assert_max_width_ramp, run_max_width_ramp
from solution import Solution

# %%
# Example test case
nums = [6, 0, 8, 2, 1, 5]
expected = 4

# %%
result = run_max_width_ramp(Solution, nums)
result

# %%
assert_max_width_ramp(result, expected)
