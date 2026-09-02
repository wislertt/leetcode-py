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
from helpers import assert_compute_area, run_compute_area
from solution import Solution

# %%
# Example test case
ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
expected = 45

# %%
result = run_compute_area(Solution, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
result

# %%
assert_compute_area(result, expected)
