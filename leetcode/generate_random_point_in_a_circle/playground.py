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
from helpers import assert_rand_point, run_rand_point
from solution import Solution

# %%
# Example test case
radius = 1.0
x_center = 0.0
y_center = 0.0
seed = 42
n = 20

# %%
result = run_rand_point(Solution, radius, x_center, y_center, seed, n)
result

# %%
assert_rand_point(result, radius, x_center, y_center, n)
