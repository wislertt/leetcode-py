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
from helpers import assert_prime_sub_operation, run_prime_sub_operation
from solution import Solution

# %%
# Example test case
nums = [4, 9, 6, 10]
expected = True

# %%
result = run_prime_sub_operation(Solution, nums)
result

# %%
assert_prime_sub_operation(result, expected)
