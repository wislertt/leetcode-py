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
from helpers import assert_reaching_points, run_reaching_points
from solution import Solution

# %%
# Example test case
sx = 1
sy = 1
tx = 3
ty = 5
expected = True

# %%
result = run_reaching_points(Solution, sx, sy, tx, ty)
result

# %%
assert_reaching_points(result, expected)
