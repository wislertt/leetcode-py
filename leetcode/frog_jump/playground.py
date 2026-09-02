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
from helpers import assert_can_cross, run_can_cross
from solution import Solution

# %%
# Example test case
stones = [0, 1, 3, 5, 6, 8, 12, 17]
expected = True

# %%
result = run_can_cross(Solution, stones)
result

# %%
assert_can_cross(result, expected)
