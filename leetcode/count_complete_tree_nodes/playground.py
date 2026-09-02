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
from helpers import assert_count_nodes, run_count_nodes
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, 4, 5, 6]
expected = 6

# %%
result = run_count_nodes(Solution, root_list)
result

# %%
assert_count_nodes(result, expected)
