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
from helpers import assert_largest_combination, run_largest_combination
from solution import Solution

# %%
# Example test case
candidates = [16, 17, 71, 62, 12, 24, 14]
expected = 4

# %%
result = run_largest_combination(Solution, candidates)
result

# %%
assert_largest_combination(result, expected)
