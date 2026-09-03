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
from helpers import assert_count_prime_set_bits, run_count_prime_set_bits
from solution import Solution

# %%
# Example test case
left: int = 6
right: int = 10
expected: int = 4

# %%
result = run_count_prime_set_bits(Solution, left, right)
result

# %%
assert_count_prime_set_bits(result, expected)
