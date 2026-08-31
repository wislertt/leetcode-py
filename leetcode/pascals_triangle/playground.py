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
from helpers import assert_generate, run_generate
from solution import Solution

# %%
# Example test case
num_rows: int = 5
expected: list[list[int]] = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# %%
result = run_generate(Solution, num_rows)
result

# %%
assert_generate(result, expected)
