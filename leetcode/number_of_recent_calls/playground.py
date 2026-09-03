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
from helpers import assert_recent_counter, run_recent_counter
from solution import RecentCounter

# %%
# Example test case
operations = ["RecentCounter", "ping", "ping", "ping", "ping"]
inputs = [[], [1], [100], [3001], [3002]]
expected = [None, 1, 2, 3, 3]

# %%
result, counter = run_recent_counter(RecentCounter, operations, inputs)
print(result)
counter

# %%
assert_recent_counter(result, expected)
