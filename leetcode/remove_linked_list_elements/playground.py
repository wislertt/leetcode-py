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
from helpers import assert_remove_linked_list_elements, run_remove_linked_list_elements
from solution import Solution

# %%
# Example test case
head_vals: list[int] = [1, 2, 6, 3, 4, 5, 6]
val: int = 6
expected_vals: list[int] = [1, 2, 3, 4, 5]

# %%
result = run_remove_linked_list_elements(Solution, head_vals, val)
result

# %%
assert_remove_linked_list_elements(result, expected_vals)
