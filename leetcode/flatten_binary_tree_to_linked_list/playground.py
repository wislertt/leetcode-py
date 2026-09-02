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
from helpers import assert_flatten, run_flatten
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 5, 3, 4, None, 6]
expected = [1, None, 2, None, 3, None, 4, None, 5, None, 6]

# %%
result = run_flatten(Solution, root_list)
result

# %%
assert_flatten(result, expected)
