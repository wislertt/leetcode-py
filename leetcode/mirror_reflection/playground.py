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
from helpers import assert_mirror_reflection, run_mirror_reflection
from solution import Solution

# %%
# Example test case
p = 2
q = 1
expected = 2

# %%
result = run_mirror_reflection(Solution, p, q)
result

# %%
assert_mirror_reflection(result, expected)
