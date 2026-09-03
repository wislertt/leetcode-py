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
from helpers import assert_is_cousins, run_is_cousins
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, 4]
x = 4
y = 3
expected = False

# %%
result = run_is_cousins(Solution, root_list, x, y)
result

# %%
assert_is_cousins(result, expected)
