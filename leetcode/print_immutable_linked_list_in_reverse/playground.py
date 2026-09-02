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
from helpers import assert_print_linked_list_in_reverse, run_print_linked_list_in_reverse
from solution import Solution

# %%
# Example test case
values = [1, 2, 3, 4]
expected = [4, 3, 2, 1]

# %%
result = run_print_linked_list_in_reverse(Solution, values)
result

# %%
assert_print_linked_list_in_reverse(result, expected)
