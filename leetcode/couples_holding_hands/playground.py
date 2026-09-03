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
from helpers import assert_min_swaps_couples, run_min_swaps_couples
from solution import Solution

# %%
# Example test case
row: list[int] = [0, 2, 1, 3]
expected = 1

# %%
result = run_min_swaps_couples(Solution, row)
result

# %%
assert_min_swaps_couples(result, expected)
