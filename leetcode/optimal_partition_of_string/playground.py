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
from helpers import assert_partition_string, run_partition_string
from solution import Solution

# %%
# Example test case
s = "abacaba"
expected = 4

# %%
result = run_partition_string(Solution, s)
result

# %%
assert_partition_string(result, expected)
