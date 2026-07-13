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
from helpers import assert_is_symmetric, run_is_symmetric
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 2, 3, 4, 4, 3]
expected = True

# %%
result = run_is_symmetric(Solution, root_list)
result

# %%
assert_is_symmetric(result, expected)
