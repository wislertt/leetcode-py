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
from helpers import assert_reverse_odd_levels, run_reverse_odd_levels
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [2, 3, 5, 8, 13, 21, 34]
expected_list: list[int | None] = [2, 5, 3, 8, 13, 21, 34]

# %%
result = run_reverse_odd_levels(Solution, root_list)
result

# %%
assert_reverse_odd_levels(result, expected_list)
