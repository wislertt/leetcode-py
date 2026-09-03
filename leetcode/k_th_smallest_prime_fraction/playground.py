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
from helpers import assert_kth_smallest_prime_fraction, run_kth_smallest_prime_fraction
from solution import Solution

# %%
# Example test case
arr = [1, 2, 3, 5]
k = 3
expected = [2, 5]

# %%
result = run_kth_smallest_prime_fraction(Solution, arr, k)
result

# %%
assert_kth_smallest_prime_fraction(result, expected)
