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
from helpers import assert_bag_of_tokens_score, run_bag_of_tokens_score
from solution import Solution

# %%
# Example test case
tokens = [100, 200, 300, 400]
power = 200
expected = 2

# %%
result = run_bag_of_tokens_score(Solution, tokens, power)
result

# %%
assert_bag_of_tokens_score(result, expected)
