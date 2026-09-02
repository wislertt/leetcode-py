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
from helpers import assert_pick, run_pick
from solution import Solution

# %%
# Example test case
rects = [[-2, -2, 1, 1], [2, 2, 4, 6]]
seed = 0
n = 20

# %%
result = run_pick(Solution, rects, seed, n)
print(result)
result

# %%
assert_pick(result, rects, n)
