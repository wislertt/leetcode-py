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
from helpers import assert_valid_square, run_valid_square
from solution import Solution

# %%
# Example test case
p1 = [0, 0]
p2 = [1, 1]
p3 = [1, 0]
p4 = [0, 1]
expected = True

# %%
result = run_valid_square(Solution, p1, p2, p3, p4)
result

# %%
assert_valid_square(result, expected)
