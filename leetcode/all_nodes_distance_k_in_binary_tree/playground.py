# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_distance_k, run_distance_k
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
target = 5
k = 2
expected = [7, 4, 1]

# %%
result = run_distance_k(Solution, root_list, target, k)
result

# %%
assert_distance_k(result, expected)
