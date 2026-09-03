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
n = 7
blacklist = [2, 3, 5]
seed = 0
calls = 8

# %%
result = run_pick(Solution, n, blacklist, seed, calls)
print(result)
result

# %%
assert_pick(result, n, blacklist, calls)
