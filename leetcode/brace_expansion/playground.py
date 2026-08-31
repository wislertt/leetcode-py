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
from helpers import assert_expand, run_expand
from solution import Solution

# %%
# Example test case
s = "{a,b}c{d,e}f"
expected = ["acdf", "acef", "bcdf", "bcef"]

# %%
result = run_expand(Solution, s)
result

# %%
assert_expand(result, expected)
