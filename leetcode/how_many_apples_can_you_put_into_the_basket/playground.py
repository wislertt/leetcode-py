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
from helpers import assert_max_number_of_apples, run_max_number_of_apples
from solution import Solution

# %%
# Example test case
weight = [100, 200, 150, 1000]
expected = 4

# %%
result = run_max_number_of_apples(Solution, weight)
result

# %%
assert_max_number_of_apples(result, expected)
