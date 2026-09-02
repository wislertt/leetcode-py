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
from helpers import assert_length_longest_path, run_length_longest_path
from solution import Solution

# %%
# Example test case
input_str = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
expected = 20

# %%
result = run_length_longest_path(Solution, input_str)
result

# %%
assert_length_longest_path(result, expected)
