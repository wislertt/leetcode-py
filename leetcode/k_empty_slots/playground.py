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
from helpers import assert_k_empty_slots, run_k_empty_slots
from solution import Solution

# %%
# Example test case
bulbs = [1, 3, 2]
k = 1
expected = 2

# %%
result = run_k_empty_slots(Solution, bulbs, k)
result

# %%
assert_k_empty_slots(result, expected)
