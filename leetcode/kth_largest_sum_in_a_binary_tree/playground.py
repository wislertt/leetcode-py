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
from helpers import assert_kth_largest_level_sum, run_kth_largest_level_sum
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [5, 8, 9, 2, 1, 3, 7, 4, 6]
k = 2
expected = 13

# %%
result = run_kth_largest_level_sum(Solution, root_list, k)
result

# %%
assert_kth_largest_level_sum(result, expected)
