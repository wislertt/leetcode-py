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
from helpers import assert_two_sum, run_two_sum
from solution import TwoSum

# %%
# Example test case
operations = ["TwoSum", "add", "add", "add", "find", "find"]
inputs = [[], [1], [3], [5], [4], [7]]
expected = [None, None, None, None, True, False]

# %%
result, two_sum = run_two_sum(TwoSum, operations, inputs)
print(result)
two_sum

# %%
assert_two_sum(result, expected)
