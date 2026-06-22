# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_good_nodes, run_good_nodes
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [3, 1, 4, 3, None, 1, 5]
expected = 4

# %%
result = run_good_nodes(Solution, root_list)
result

# %%
assert_good_nodes(result, expected)
