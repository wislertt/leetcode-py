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
from helpers import assert_count_pairs, run_count_pairs
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, None, 4]
distance = 3
expected = 1

# %%
result = run_count_pairs(Solution, root_list, distance)
result

# %%
assert_count_pairs(result, expected)
