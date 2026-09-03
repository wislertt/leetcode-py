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
from helpers import assert_is_rectangle_overlap, run_is_rectangle_overlap
from solution import Solution

# %%
# Example test case
rec1 = [0, 0, 2, 2]
rec2 = [1, 1, 3, 3]
expected = True

# %%
result = run_is_rectangle_overlap(Solution, rec1, rec2)
result

# %%
assert_is_rectangle_overlap(result, expected)
