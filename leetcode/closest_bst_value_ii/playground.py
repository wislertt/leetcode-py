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
from helpers import assert_closest_k_values, run_closest_k_values
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [4, 2, 5, 1, 3]
target = 3.714286
k = 2
expected = [3, 4]

# %%
result = run_closest_k_values(Solution, root_list, target, k)
result

# %%
assert_closest_k_values(result, expected)
