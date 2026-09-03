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
from helpers import assert_num_friend_requests, run_num_friend_requests
from solution import Solution

# %%
# Example test case
ages = [16, 16]
expected = 2

# %%
result = run_num_friend_requests(Solution, ages)
result

# %%
assert_num_friend_requests(result, expected)
