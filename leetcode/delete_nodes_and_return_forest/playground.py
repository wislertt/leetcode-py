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
from helpers import assert_del_nodes, run_del_nodes
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, 4, 5, 6, 7]
to_delete = [3, 5]
expected_forest = [[1, 2, None, 4], [6], [7]]

# %%
result = run_del_nodes(Solution, root_list, to_delete)
result

# %%
assert_del_nodes(result, expected_forest)
