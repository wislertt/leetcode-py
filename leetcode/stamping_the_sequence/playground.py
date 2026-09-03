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
from helpers import assert_moves_to_stamp, run_moves_to_stamp
from solution import Solution

# %%
# Example test case
stamp = "abc"
target = "ababc"
expected = [0, 2]

# %%
result = run_moves_to_stamp(Solution, stamp, target)
result

# %%
assert_moves_to_stamp(result, expected, stamp, target)
