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
from helpers import assert_poor_pigs, run_poor_pigs
from solution import Solution

# %%
# Example test case
buckets: int = 4
minutes_to_die: int = 15
minutes_to_test: int = 15
expected: int = 2

# %%
result = run_poor_pigs(Solution, buckets, minutes_to_die, minutes_to_test)
result

# %%
assert_poor_pigs(result, expected)
