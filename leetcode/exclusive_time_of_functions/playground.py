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
from helpers import assert_exclusive_time, run_exclusive_time
from solution import Solution

# %%
# Example test case
n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
expected = [3, 4]

# %%
result = run_exclusive_time(Solution, n, logs)
result

# %%
assert_exclusive_time(result, expected)
