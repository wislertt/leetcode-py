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
from helpers import assert_probability_of_heads, run_probability_of_heads
from solution import Solution

# %%
# Example test case
prob = [0.4]
target = 1
expected = 0.4

# %%
result = run_probability_of_heads(Solution, prob, target)
result

# %%
assert_probability_of_heads(result, expected)
