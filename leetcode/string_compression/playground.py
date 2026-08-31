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
from helpers import assert_compress, run_compress
from solution import Solution

# %%
# Example test case
chars = ["a", "a", "b", "b", "c", "c", "c"]
expected = ["a", "2", "b", "2", "c", "3"]

# %%
result = run_compress(Solution, chars)
result

# %%
assert_compress(result, expected)
