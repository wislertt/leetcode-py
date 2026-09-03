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
from helpers import assert_average_of_levels, run_average_of_levels
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
expected = [3.0, 14.5, 11.0]

# %%
result = run_average_of_levels(Solution, root_list)
result

# %%
assert_average_of_levels(result, expected)
