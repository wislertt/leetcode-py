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
from helpers import assert_h_index, run_h_index
from solution import Solution

# %%
# Example test case
citations = [3, 0, 6, 1, 5]
expected = 3

# %%
result = run_h_index(Solution, citations)
result

# %%
assert_h_index(result, expected)
