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
from helpers import assert_min_swaps, run_min_swaps
from solution import Solution

# %%
# Example test case
s = "][]["
expected = 1

# %%
result = run_min_swaps(Solution, s)
result

# %%
assert_min_swaps(result, expected)
