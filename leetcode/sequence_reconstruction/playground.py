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
from helpers import assert_sequence_reconstruction, run_sequence_reconstruction
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3]
sequences = [[1, 2], [1, 3], [2, 3]]
expected = True

# %%
result = run_sequence_reconstruction(Solution, nums, sequences)
result

# %%
assert_sequence_reconstruction(result, expected)
