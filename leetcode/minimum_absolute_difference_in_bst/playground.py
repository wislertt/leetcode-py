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
from helpers import assert_get_minimum_difference, run_get_minimum_difference
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [4, 2, 6, 1, 3]
expected = 1

# %%
result = run_get_minimum_difference(Solution, root_list)
result

# %%
assert_get_minimum_difference(result, expected)
