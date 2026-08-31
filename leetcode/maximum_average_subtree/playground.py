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
from helpers import assert_maximum_average_subtree, run_maximum_average_subtree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [5, 6, 1]
expected = 6.0

# %%
result = run_maximum_average_subtree(Solution, root_list)
result

# %%
assert_maximum_average_subtree(result, expected)
