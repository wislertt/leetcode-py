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
from helpers import assert_is_self_crossing, run_is_self_crossing
from solution import Solution

# %%
# Example test case
distance = [2, 1, 1, 2]
expected = True

# %%
result = run_is_self_crossing(Solution, distance)
result

# %%
assert_is_self_crossing(result, expected)
