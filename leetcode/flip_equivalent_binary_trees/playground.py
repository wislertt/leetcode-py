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
from helpers import assert_flip_equiv, run_flip_equiv
from solution import Solution

# %%
# Example test case
root1_list: list[int | None] = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8]
root2_list: list[int | None] = [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]
expected = True

# %%
result = run_flip_equiv(Solution, root1_list, root2_list)
result

# %%
assert_flip_equiv(result, expected)
