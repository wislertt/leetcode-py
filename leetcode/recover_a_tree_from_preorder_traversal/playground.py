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
from helpers import assert_recover_from_preorder, run_recover_from_preorder
from solution import Solution

# %%
# Example test case
traversal = "1-2--3--4-5--6--7"
expected_list: list[int | None] = [1, 2, 5, 3, 4, 6, 7]

# %%
result = run_recover_from_preorder(Solution, traversal)
result

# %%
assert_recover_from_preorder(result, expected_list)
