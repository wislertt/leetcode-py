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
from helpers import assert_min_camera_cover, run_min_camera_cover
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [0, 0, None, 0, 0]
expected = 1

# %%
result = run_min_camera_cover(Solution, root_list)
result

# %%
assert_min_camera_cover(result, expected)
