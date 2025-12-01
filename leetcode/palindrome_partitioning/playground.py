# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_partition, run_partition
from solution import Solution

# %%
# Example test case
s = "aab"
expected = [["a", "a", "b"], ["aa", "b"]]

# %%
result = run_partition(Solution, s)
result

# %%
assert_partition(result, expected)
