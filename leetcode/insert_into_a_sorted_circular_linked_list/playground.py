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
from helpers import assert_insert, run_insert
from solution import Solution

# %%
# Example test case
head_list = [3, 4, 1]
insert_val = 2
expected_list = [3, 4, 1, 2]

# %%
result = run_insert(Solution, head_list, insert_val)
result

# %%
assert_insert(result, expected_list)
