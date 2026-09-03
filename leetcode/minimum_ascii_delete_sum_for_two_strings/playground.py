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
from helpers import assert_minimum_delete_sum, run_minimum_delete_sum
from solution import Solution

# %%
# Example test case
s1 = "sea"
s2 = "eat"
expected = 231

# %%
result = run_minimum_delete_sum(Solution, s1, s2)
result

# %%
assert_minimum_delete_sum(result, expected)
