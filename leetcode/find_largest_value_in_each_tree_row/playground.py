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
from helpers import assert_largest_values, run_largest_values
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 3, 2, 5, 3, None, 9]
expected = [1, 3, 9]

# %%
result = run_largest_values(Solution, root_list)
result

# %%
assert_largest_values(result, expected)
