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
from helpers import assert_trim_bst, run_trim_bst
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 0, 2]
low = 1
high = 2
expected_list: list[int | None] = [1, None, 2]

# %%
result = run_trim_bst(Solution, root_list, low, high)
result

# %%
assert_trim_bst(result, expected_list)
