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
from helpers import assert_longest_consecutive, run_longest_consecutive
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [2, 1, 3]
expected = 3

# %%
result = run_longest_consecutive(Solution, root_list)
result

# %%
assert_longest_consecutive(result, expected)
