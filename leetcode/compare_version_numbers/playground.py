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
from helpers import assert_compare_version, run_compare_version
from solution import Solution

# %%
# Example test case
version1 = "1.01"
version2 = "1.001"
expected = 0

# %%
result = run_compare_version(Solution, version1, version2)
result

# %%
assert_compare_version(result, expected)
