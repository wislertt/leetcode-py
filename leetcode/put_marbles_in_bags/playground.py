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
from helpers import assert_put_marbles, run_put_marbles
from solution import Solution

# %%
# Example test case
weights: list[int] = [1, 3, 5, 1]
k = 2
expected = 4

# %%
result = run_put_marbles(Solution, weights, k)
result

# %%
assert_put_marbles(result, expected)
