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
from helpers import assert_fair_candy_swap, run_fair_candy_swap
from solution import Solution

# %%
# Example test case
alice_sizes = [1, 1]
bob_sizes = [2, 2]
expected = [1, 2]

# %%
result = run_fair_candy_swap(Solution, alice_sizes, bob_sizes)
result

# %%
assert_fair_candy_swap(result, expected)
