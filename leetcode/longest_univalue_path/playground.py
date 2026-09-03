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
from helpers import assert_longest_univalue_path, run_longest_univalue_path
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [5, 4, 5, 1, 1, None, 5]
expected = 2

# %%
result = run_longest_univalue_path(Solution, root_list)
result

# %%
assert_longest_univalue_path(result, expected)
