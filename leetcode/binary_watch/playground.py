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
from helpers import assert_read_binary_watch, run_read_binary_watch
from solution import Solution

# %%
# Example test case
turned_on = 1
expected = ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]

# %%
result = run_read_binary_watch(Solution, turned_on)
result

# %%
assert_read_binary_watch(result, expected)
