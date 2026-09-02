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
    assert_longest_substring_with_at_least_k_repeating_characters,
    run_longest_substring_with_at_least_k_repeating_characters,
)
from solution import Solution

# %%
# Example test case
s = "aaabb"
k = 3
expected = 3

# %%
result = run_longest_substring_with_at_least_k_repeating_characters(Solution, s, k)
result

# %%
assert_longest_substring_with_at_least_k_repeating_characters(result, expected)
