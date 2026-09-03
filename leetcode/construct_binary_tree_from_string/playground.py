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
from helpers import assert_str2tree, run_str2tree
from solution import Solution

# %%
# Example test case
s = "4(2(3)(1))(6(5))"
expected_list: list[int | None] = [4, 2, 6, 3, 1, 5]

# %%
result = run_str2tree(Solution, s)
result

# %%
assert_str2tree(result, expected_list)
