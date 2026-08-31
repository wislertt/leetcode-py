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
from helpers import assert_has_path_sum, run_has_path_sum
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
target_sum: int = 22
expected: bool = True

# %%
result = run_has_path_sum(Solution, root_list, target_sum)
result

# %%
assert_has_path_sum(result, expected)
