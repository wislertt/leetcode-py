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
from helpers import assert_path_sum, run_path_sum
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
target_sum = 8
expected = 3

# %%
result = run_path_sum(Solution, root_list, target_sum)
result

# %%
assert_path_sum(result, expected)
