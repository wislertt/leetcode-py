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
from helpers import assert_find_target, run_find_target
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [5, 3, 6, 2, 4, None, 7]
k = 9
expected = True

# %%
result = run_find_target(Solution, root_list, k)
result

# %%
assert_find_target(result, expected)
