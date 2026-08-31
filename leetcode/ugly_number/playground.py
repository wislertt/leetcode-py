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
from helpers import assert_is_ugly, run_is_ugly
from solution import Solution

# %%
# Example test case
n = 6
expected = True

# %%
result = run_is_ugly(Solution, n)
result

# %%
assert_is_ugly(result, expected)
