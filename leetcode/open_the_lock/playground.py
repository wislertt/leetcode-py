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
from helpers import assert_open_lock, run_open_lock
from solution import Solution

# %%
# Example test case
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
expected = 6

# %%
result = run_open_lock(Solution, deadends, target)
result

# %%
assert_open_lock(result, expected)
