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
from helpers import assert_minimum_recolors, run_minimum_recolors
from solution import Solution

# %%
# Example test case
blocks = "WBBWWBBWBW"
k = 7
expected = 3

# %%
result = run_minimum_recolors(Solution, blocks, k)
result

# %%
assert_minimum_recolors(result, expected)
