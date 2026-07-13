# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_hit_counter, run_hit_counter
from solution import HitCounter

# %%
# Example test case
operations = ["HitCounter", "hit", "hit", "hit", "get_hits", "hit", "get_hits", "get_hits"]
inputs = [[], [1], [2], [3], [4], [300], [300], [301]]
expected = [None, None, None, None, 3, None, 4, 3]

# %%
result, counter = run_hit_counter(HitCounter, operations, inputs)
print(result)
counter

# %%
assert_hit_counter(result, expected)
