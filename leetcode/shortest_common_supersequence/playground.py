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
from helpers import assert_shortest_common_supersequence, run_shortest_common_supersequence
from solution import Solution

# %%
# Example test case
str1 = "abac"
str2 = "cab"
expected_length = 5

# %%
result = run_shortest_common_supersequence(Solution, str1, str2)
result

# %%
assert_shortest_common_supersequence(result, str1, str2, expected_length)
