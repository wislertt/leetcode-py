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
from helpers import assert_has_group_size_x, run_has_group_size_x
from solution import Solution

# %%
# Example test case
deck = [1, 2, 3, 4, 4, 3, 2, 1]
expected = True

# %%
result = run_has_group_size_x(Solution, deck)
result

# %%
assert_has_group_size_x(result, expected)
