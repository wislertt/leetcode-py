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
from helpers import assert_find_restaurant, run_find_restaurant
from solution import Solution

# %%
# Example test case
list1 = ["happy", "sad", "good"]
list2 = ["sad", "happy", "good"]
expected = ["sad", "happy"]

# %%
result = run_find_restaurant(Solution, list1, list2)
result

# %%
assert_find_restaurant(result, expected)
