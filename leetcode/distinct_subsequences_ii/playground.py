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
from helpers import assert_distinct_subseq_ii, run_distinct_subseq_ii
from solution import Solution

# %%
# Example test case
s = "abc"
expected = 7

# %%
result = run_distinct_subseq_ii(Solution, s)
result

# %%
assert_distinct_subseq_ii(result, expected)
