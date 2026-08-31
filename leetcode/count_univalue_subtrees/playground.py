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
from helpers import assert_count_unival_subtrees, run_count_unival_subtrees
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [5, 1, 5, 5, 5, None, 5]
expected = 4

# %%
result = run_count_unival_subtrees(Solution, root_list)
result

# %%
assert_count_unival_subtrees(result, expected)
