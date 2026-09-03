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
from helpers import assert_k_similarity, run_k_similarity
from solution import Solution

# %%
# Example test case
s1 = "abc"
s2 = "bca"
expected = 2

# %%
result = run_k_similarity(Solution, s1, s2)
result

# %%
assert_k_similarity(result, expected)
