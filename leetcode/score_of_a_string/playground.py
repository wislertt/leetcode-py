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
from helpers import assert_score_of_string, run_score_of_string
from solution import Solution

# %%
# Example test case
s = "hello"
expected = 13

# %%
result = run_score_of_string(Solution, s)
result

# %%
assert_score_of_string(result, expected)
