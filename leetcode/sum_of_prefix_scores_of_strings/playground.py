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
from helpers import assert_sum_prefix_scores, run_sum_prefix_scores
from solution import Solution

# %%
# Example test case
words = ["abc", "ab", "bc", "b"]
expected = [5, 4, 3, 2]

# %%
result = run_sum_prefix_scores(Solution, words)
result

# %%
assert_sum_prefix_scores(result, expected)
