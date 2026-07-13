# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_asteroid_collision, run_asteroid_collision
from solution import Solution

# %%
# Example test case
asteroids = [5, 10, -5]
expected = [5, 10]

# %%
result = run_asteroid_collision(Solution, asteroids)
result

# %%
assert_asteroid_collision(result, expected)
