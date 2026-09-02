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
from helpers import assert_delete_duplicates, run_delete_duplicates
from solution import Solution

# %%
# Example test case
head_list = [1, 2, 3, 3, 4, 4, 5]
expected_list = [1, 2, 5]

# %%
result = run_delete_duplicates(Solution, head_list)
result

# %%
assert_delete_duplicates(result, expected_list)
