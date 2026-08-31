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
from helpers import assert_validate_stack_sequences, run_validate_stack_sequences
from solution import Solution

# %%
# Example test case
pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
expected = True

# %%
result = run_validate_stack_sequences(Solution, pushed, popped)
result

# %%
assert_validate_stack_sequences(result, expected)
