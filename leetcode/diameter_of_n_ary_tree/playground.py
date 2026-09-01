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
from helpers import assert_diameter, run_diameter
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, None, 3, 2, 4, None, 5, 6]
expected = 3

# %%
result = run_diameter(Solution, root_list)
result

# %%
assert_diameter(result, expected)
