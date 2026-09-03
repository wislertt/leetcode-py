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
from helpers import assert_all_paths_source_target, run_all_paths_source_target
from solution import Solution

# %%
# Example test case
graph = [[1, 2], [3], [3], []]
expected = [[0, 1, 3], [0, 2, 3]]

# %%
result = run_all_paths_source_target(Solution, graph)
result

# %%
assert_all_paths_source_target(result, expected)
