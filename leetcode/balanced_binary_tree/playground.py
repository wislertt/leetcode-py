# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_is_balanced, run_is_balanced
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
expected = True

# %%
result = run_is_balanced(Solution, root_list)
result

# %%
assert_is_balanced(result, expected)
