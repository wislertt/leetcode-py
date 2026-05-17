# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_find_circle_num, run_find_circle_num
from solution import Solution

# %%
# Example test case
is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
expected = 2

# %%
result = run_find_circle_num(Solution, is_connected)
result

# %%
assert_find_circle_num(result, expected)
