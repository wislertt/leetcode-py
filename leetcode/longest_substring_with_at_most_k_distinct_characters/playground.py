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
from helpers import (
    assert_length_of_longest_substring_k_distinct,
    run_length_of_longest_substring_k_distinct,
)
from solution import Solution

# %%
# Example test case
s = "eceba"
k = 2
expected = 3

# %%
result = run_length_of_longest_substring_k_distinct(Solution, s, k)
result

# %%
assert_length_of_longest_substring_k_distinct(result, expected)
