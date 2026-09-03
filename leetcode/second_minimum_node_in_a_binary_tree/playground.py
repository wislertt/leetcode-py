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
from helpers import assert_find_second_minimum_value, run_find_second_minimum_value
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [2, 2, 5, None, None, 5, 7]
expected = 5

# %%
result = run_find_second_minimum_value(Solution, root_list)
result

# %%
assert_find_second_minimum_value(result, expected)
