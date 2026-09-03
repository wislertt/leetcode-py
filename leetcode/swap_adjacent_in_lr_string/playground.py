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
from helpers import assert_can_transform, run_can_transform
from solution import Solution

# %%
# Example test case
start = "RXXLRXRXL"
result = "XRLXXRRLX"
expected = True

# %%
result = run_can_transform(Solution, start, result)
result

# %%
assert_can_transform(result, expected)
