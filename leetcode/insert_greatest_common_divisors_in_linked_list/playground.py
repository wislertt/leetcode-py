# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_insert_greatest_common_divisors, run_insert_greatest_common_divisors
from solution import Solution

# %%
# Example test case
head_list = [18, 6, 10, 3]
expected_list = [18, 6, 6, 2, 10, 1, 3]

# %%
result = run_insert_greatest_common_divisors(Solution, head_list)
result

# %%
assert_insert_greatest_common_divisors(result, expected_list)
