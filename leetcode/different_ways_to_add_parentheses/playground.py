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
from helpers import assert_diff_ways_to_compute, run_diff_ways_to_compute
from solution import Solution

# %%
# Example test case
expression = "2-1-1"
expected = [0, 2]

# %%
result = run_diff_ways_to_compute(Solution, expression)
result

# %%
assert_diff_ways_to_compute(result, expected)
