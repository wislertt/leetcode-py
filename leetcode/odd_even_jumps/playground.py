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
from helpers import assert_odd_even_jumps, run_odd_even_jumps
from solution import Solution

# %%
# Example test case
arr = [10, 13, 12, 14, 15]
expected = 2

# %%
result = run_odd_even_jumps(Solution, arr)
result

# %%
assert_odd_even_jumps(result, expected)
