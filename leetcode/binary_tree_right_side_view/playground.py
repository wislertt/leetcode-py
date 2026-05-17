# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_right_side_view, run_right_side_view
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, None, 5, None, 4]
expected = [1, 3, 4]

# %%
result = run_right_side_view(Solution, root_list)
result

# %%
assert_right_side_view(result, expected)
