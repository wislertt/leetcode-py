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
from helpers import assert_num_of_minutes, run_num_of_minutes
from solution import Solution

# %%
# Example test case
n = 6
head_id = 2
manager = [2, 2, -1, 2, 2, 2]
inform_time = [0, 0, 1, 0, 0, 0]
expected = 1

# %%
result = run_num_of_minutes(Solution, n, head_id, manager, inform_time)
result

# %%
assert_num_of_minutes(result, expected)
