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
from helpers import assert_tallest_billboard, run_tallest_billboard
from solution import Solution

# %%
# Example test case
rods = [1, 2, 3, 6]
expected = 6

# %%
result = run_tallest_billboard(Solution, rods)
result

# %%
assert_tallest_billboard(result, expected)
