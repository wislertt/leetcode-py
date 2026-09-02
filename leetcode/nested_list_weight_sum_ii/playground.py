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
from typing import Any

from helpers import assert_depth_sum_inverse, run_depth_sum_inverse
from solution import Solution

# %%
# Example test case
nested_list: list[Any] = [[1, 1], 2, [1, 1]]
expected = 8

# %%
result = run_depth_sum_inverse(Solution, nested_list)
result

# %%
assert_depth_sum_inverse(result, expected)
