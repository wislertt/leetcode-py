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
from helpers import assert_tree2str, run_tree2str
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, 4]
expected = "1(2(4))(3)"

# %%
result = run_tree2str(Solution, root_list)
result

# %%
assert_tree2str(result, expected)
