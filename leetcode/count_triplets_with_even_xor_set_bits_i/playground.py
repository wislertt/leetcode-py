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
from helpers import assert_triplet_count, run_triplet_count
from solution import Solution

# %%
# Example test case
a = [1]
b = [2]
c = [3]
expected = 1

# %%
result = run_triplet_count(Solution, a, b, c)
result

# %%
assert_triplet_count(result, expected)
