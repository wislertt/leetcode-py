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
from helpers import assert_reconstruct_queue, run_reconstruct_queue
from solution import Solution

# %%
# Example test case
people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
expected = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

# %%
result = run_reconstruct_queue(Solution, people)
result

# %%
assert_reconstruct_queue(result, expected)
