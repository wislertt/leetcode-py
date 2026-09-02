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
from helpers import assert_two_sum_bsts, run_two_sum_bsts
from solution import Solution

# %%
# Example test case
root1_list: list[int | None] = [2, 1, 4]
root2_list: list[int | None] = [1, 0, 3]
target = 5
expected = True

# %%
result = run_two_sum_bsts(Solution, root1_list, root2_list, target)
result

# %%
assert_two_sum_bsts(result, expected)
