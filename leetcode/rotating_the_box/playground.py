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
from helpers import assert_rotate_the_box, run_rotate_the_box
from solution import Solution

# %%
# Example test case
box_grid = [["#", ".", "#"]]
expected = [["."], ["#"], ["#"]]

# %%
result = run_rotate_the_box(Solution, box_grid)
result

# %%
assert_rotate_the_box(result, expected)
