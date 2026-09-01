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
from helpers import assert_get_directions, run_get_directions
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [5, 1, 2, 3, None, 6, 4]
start_value = 3
dest_value = 6
expected = "UURL"

# %%
result = run_get_directions(Solution, root_list, start_value, dest_value)
result

# %%
assert_get_directions(result, expected)
