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
from helpers import assert_len_longest_fib_subsequence, run_len_longest_fib_subsequence
from solution import Solution

# %%
# Example test case
arr = [1, 2, 3, 4, 5, 6, 7, 8]
expected = 5

# %%
result = run_len_longest_fib_subsequence(Solution, arr)
result

# %%
assert_len_longest_fib_subsequence(result, expected)
