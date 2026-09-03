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
from helpers import assert_flip_match_voyage, run_flip_match_voyage
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3]
voyage = [1, 3, 2]
expected = [1]

# %%
result = run_flip_match_voyage(Solution, root_list)
result

# %%
assert_flip_match_voyage(result, expected)
