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
from helpers import assert_range_sum_bst, run_range_sum_bst
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [10, 5, 15, 3, 7, None, 18]
low = 7
high = 15
expected = 32

# %%
result = run_range_sum_bst(Solution, root_list, low, high)
result

# %%
assert_range_sum_bst(result, expected)
