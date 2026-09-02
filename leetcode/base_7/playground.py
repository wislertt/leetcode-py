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
from helpers import assert_convert_to_base_7, run_convert_to_base_7
from solution import Solution

# %%
# Example test case
num = 100
expected = "202"

# %%
result = run_convert_to_base_7(Solution, num)
result

# %%
assert_convert_to_base_7(result, expected)
